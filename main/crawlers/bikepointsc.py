from main.crawlers.main import Main
from main.helpers.price import convert_price

from bs4 import BeautifulSoup


class StoreBikePointSC(Main):

    store = "BikePointSC"
    url_domain_https = "https://www.bikepointsc.com"
    url_domain_http = "http://www.bikepointsc.com"

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
                price = self.result.select(".valores")[0].text.split("Por: ")[1]
            except IndexError:
                price = self.result.select(".valores")[0].s.text.split("De: ")[1]
            except Exception:
                price = None
            price = convert_price(price)
            self._price = price
        return self._price

    @property
    def description(self):
        if not hasattr(self, "_description"):
            try:
                self._description = None
            except Exception:
                self._description = None
        return self._description

    @property
    def image(self):
        if not hasattr(self, "_image"):
            try:
                self._image = self.result.find(id="zoom1").img.get("src")
            except Exception:
                self._image = None
        return self._image

    def _extract_page(self):
        return super()._request_page(self.url)

    def _extract_result(self):
        return BeautifulSoup(self.page, "html.parser")

    def display_attributes(self):
        return super().show_attributes(self)