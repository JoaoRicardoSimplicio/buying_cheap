from main.crawlers.main import Main

from bs4 import BeautifulSoup


class StoreAmazon(Main):

    store = "Amazon"
    url_domain_https = "https://www.amazon.com"
    url_domain_http = "http://www.amazon.com"

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
                self._price = self.result.find(id="price_inside_buybox").string
            except Exception:
                self._price = None
        return self._price

    def description(self):
        if not hasattr(self, "_description"):
            try:
                pass
            except Exception:
                self._description = None
        return self._description

    def _extract_page(self):
        return super()._request_page(self.url)

    def _extract_result(self):
        return BeautifulSoup(self.page, "html.parser")
