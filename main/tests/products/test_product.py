from django.test import TestCase

from main.models import Product, PriceHistory, Store

from datetime import datetime

class TestProduct(TestCase):

    def setUp(self):
        self.store = Store.objects.create(
            name="Shop2gether"
        )
        self.product = Product.objects.create(
            name="Camisa XXYAD",
            store=self.store,
            url_product="https://shop2gether.com.br/camisa-xxyad-nike.html",
            id_product_store="",
            price_product=249.00,
            description_product="Camisa algodão cor azul",
            url_image="https://shop2gether.com.br/image/camisa-xxyad-nike.html"
        )
        self.product.pricehistory_set.create(
            price_product=299.00    
        )
        self.product.pricehistory_set.create(
            price_product=279.00
        )

    def test_product_object(self):
        self.assertIsInstance(self.product, Product)
        self.assertIsInstance(self.product.store, Store)

    def test_first_price(self):
        self.assertEqual(self.product.first_price, 299.00)

    def test_last_price(self):
        self.assertEqual(self.product.last_price, 279.00)

    def test_diff_last_two_prices(self):
        self.assertEqual(self.product.diff_last_two_prices, -30.00)

    def test_diff_first_and_last_prices(self):
        self.assertEqual(self.product.diff_first_and_last_prices, -50.00)

    def test_variance_rate_between_first_last_prices(self):
        self.assertEqual(self.product.variance_rate_between_first_last_prices, -16.722408026755854)

        

