from django.db import models
from django.contrib.postgres.fields import ArrayField


class Store(models.Model):

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url_product = models.URLField(max_length=5000, unique=True)
    id_product_store = models.CharField(max_length=100, null=True)
    price_product = models.FloatField(max_length=20)
    description_product = models.TextField(max_length=5000, null=True)
    url_image = models.URLField(max_length=500, null=True)
    sizes = ArrayField(models.CharField(max_length=255), null=True, size=10)

    @property
    def prices(self):
        return self.pricehistory_set.all().order_by("-date")

    @property
    def first_price(self):
        return self.pricehistory_set.all().first().price_product

    @property
    def last_price(self):
        return self.pricehistory_set.all().last().price_product

    @property
    def diff_last_two_prices(self):
        return self.price_product - self.last_price

    @property
    def diff_first_and_last_prices(self):
        return self.price_product - self.first_price

    @property
    def last_update_price_date(self):
        if self.pricehistory_set.filter(product=self.id).exists():
            return self.pricehistory_set.all().last().date
        return None

    @property
    def variance_rate_between_first_last_prices(self):
        if not self.diff_first_and_last_prices:
            return None
        return (self.diff_first_and_last_prices/self.first_price) * 100
        

    def __str__(self):
        return self.name


class PriceHistory(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price_product = models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.product.name} value {self.price_product}"
