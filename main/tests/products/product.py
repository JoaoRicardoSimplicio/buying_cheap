from django.test import TestCase

from main.models import Product, PriceHistory, Store

from datetime import datetime

class TestProduct(TestCase):

    def setUp(self):
        self.store = Store.objects.create(
            name="shop2gether"
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
        self.product = PriceHistory.objects.create(
            product=self.product,
            date=datetime.today(),
            price_product=279.00
        )

    def test_calculate_diff_two_last_prices(self):
        self.assertContains(self.product, diff_last_two_prices)
        self.assertEqual(self.product.diff_last_two_prices, 00.00)