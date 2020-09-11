from django.test import TestCase
from unittest import mock

from main.crawlers.kabum import StoreKabum
from main.services.product import select_store


def open_fixture_product_notebook_acer_aspire_3():
    path = "main/tests/fixtures/"
    with open(f"{path}/notebook_acer_aspire_3.html", "rb") as f:
        contents = f.read()
        return contents


class TestStoreKabum(TestCase):

    def setUp(self):
        self.store = select_store("Kabum")
        self.product = self.store(
            "https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=115252"
        )

    def test_select_correct_store(self):
        self.assertEqual(self.store, StoreKabum)

    def test_not_accept_url_from_other_domain(self):
        with self.assertRaisesMessage(Exception, "Url don't pertence this store"):
            self.store("https://www.google.com")

    def test_only_accept_valid_product_url(self):
        with self.assertRaisesMessage(Exception, "This not a valid product"):
            self.store("https://www.kabum.com.br/")

    def test_get_information_correctly(self):
        with mock.patch("main.crawlers.main.Main._request_page",
                        return_value=open_fixture_product_notebook_acer_aspire_3()
                        ):
            self.assertEqual(self.product.price, 3299.90)
            self.assertEqual(
                self.product.name, "Notebook Acer Aspire 3 Intel Core i5-10210U, 4GB, SSD 256GB, Windows 10 Home, 15.6´, Cinza - A315-54-561D | KaBuM!"
            )
            self.assertEqual(
                self.product.description,
                "Notebook Acer Aspire 3 Intel Core i5-10210U, 4GB, SSD 256GB, Windows 10 Home, 15.6´, Cinza - A315-54-561D"
            )
