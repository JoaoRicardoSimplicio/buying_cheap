from main.crawlers.main import Main
from main.helpers.price import convert_price

from bs4 import BeautifulSoup


class StoreNetshoes(Main):

    store = "Netshoes"
    url_domain_https = "https://www.netshoes.com"
    url_domain_http = "http://www.nethoes.com"

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
                price = self.result.select(".default-price")[0].string
            except IndexError:
                price = self.result.select(".default-price")[1].string
            self._price = convert_price(price)
        return self._price

    @property
    def description(self):
        if not hasattr(self, "_description"):
            try:
                self._description = self.result.find(itemprop="description").string
            except Exception:
                self._description = None
        return self._description

    @property
    def image(self):
        if not hasattr(self, "_image"):
            try:
                self._image = self.result.select(".photo-figure")[0].img.get("src")
            except Exception:
                self._image = None
        return self._image

    def _extract_page(self):
        return super()._request_page(self.url)

    def _extract_result(self):
        return BeautifulSoup(self.page, "html.parser")
