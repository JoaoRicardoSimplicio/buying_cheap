from django.test import TestCase
from unittest import mock

from main.crawlers.netshoes import StoreNetshoes
from main.services.product import select_store


def open_fixture_product_camisa_cruzeiro():
    path = "main/tests/fixtures/"
    with open(f"{path}/camisa_cruzeiro.html", "rb") as f:
        contents = f.read()
        return contents


class TestStoreNetshoe(TestCase):

    def setUp(self):
        self.store = select_store("Netshoes")
        self.product = self.store(
            "https://www.netshoes.com.br/camisa-cruzeiro-i-2021-sn-torcedor-adidas-masculina-azul-NQQ-1024-008"
        )

    def test_select_correct_store(self):
        self.assertEqual(self.store, StoreNetshoes)

    def test_not_acept_url_from_other_domain(self):
        with self.assertRaisesMessage(Exception, "Url don't pertence this store"):
            self.store("https://www.google.com")

    def test_get_information_correctly(self):
        with mock.patch("main.crawlers.main.Main._request_page",
                        return_value=open_fixture_product_camisa_cruzeiro()
                        ):
            self.assertEqual(self.product.price, 249.99)
            self.assertEqual(self.product.name, "Camisa Cruzeiro I 20/21 s/nº Torcedor Adidas Masculina - Azul | Netshoes")
