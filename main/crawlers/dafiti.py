from main.crawlers.main import Main
from main.helpers.price import convert_price

from bs4 import BeautifulSoup


class StoreDafiti(Main):

    store = "Dafiti"
    url_domain_https = "https://www.dafiti.com"
    url_domain_http = "http://www.dafiti.com"

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
                price = self.result.select(".catalog-detail-price-line")[1].span.attrs["content"]
                self._price = convert_price(price)
            except Exception:
                self._price = None
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
                self._image = self.result.select(".gallery-preview")[0].img.get("data-original")
            except Exception:
                self._image = None
        return self._image

    @property
    def avaliable_sizes(self):
        sizes = []
        if not hasattr(self, "_avaliable_sizes"):
            try:
                items = self.result.select(".product-size-selector")[0].select(".radio-options")[0].select(".product-item")
                for item in items:
                    if item.text not in sizes:
                        sizes.append(item.text)
                self._avaliable_sizes = sizes
            except Exception:
                self._avaliable_sizes = None
        return self._avaliable_sizes

    def _extract_page(self):
        return super()._request_page(self.url)

    def _extract_result(self):
        return BeautifulSoup(self.page, "html.parser")
