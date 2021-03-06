from main.crawlers.main import Main
from main.helpers.price import convert_price

from bs4 import BeautifulSoup


class StoreMercadoLivre(Main):

    store = "Mercado Livre"
    url_domain_https = "https://produto.mercadolivre.com"
    url_domain_http = "http://produto.mercadolivre.com"

    def __init__(self, url):
        if not url.startswith(self.url_domain_https):
            if not url.startswith(self.url_domain_http):
                raise Exception("Url don't pertence this store")
        self.url = url

    @property
    def page(self):
        if not hasattr(self, "_page"):
            self._page = self._extract_page()
        return self._page

    @property
    def result(self):
        if not hasattr(self, "_result"):
            self._result = self._extract_result()
        return self._result
    
    @property
    def name(self):
        if not hasattr(self, "_name"):
            try:
                self._name = self.result.title.string
            except Exception:
                self._name = None
        return self._name

    @property
    def price(self):
        if not hasattr(self, "_price"):
            try:
                self._price = self.result.select(".ui-pdp-price__second-line")[0].text
            except Exception:
                self._price = None
        return self._price

    def _extract_page(self):
        return super()._request_page(self.url)

    def _extract_result(self):
        return BeautifulSoup(self.page, "html.parser")

    def display_attributes(self):
        return super().show_attributes(self)