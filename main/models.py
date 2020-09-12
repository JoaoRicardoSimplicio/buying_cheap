from django.db import models


class Store(models.Model):

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url_product = models.URLField(max_length=500, unique=True)
    id_product_store = models.CharField(max_length=100, null=True)
    price_product = models.FloatField(max_length=20)
    description_product = models.TextField(max_length=5000)
    url_image = models.URLField(max_length=500, null=True)

    @property
    def prices(self):
        return self.pricehistory_set.all()

    @property
    def diff(self):
        last_price = self.pricehistory_set.all().last().price_product
        return self.price_product - last_price

    def __str__(self):
        return self.name


class PriceHistory(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price_product = models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.product.name} value {self.price_product}"