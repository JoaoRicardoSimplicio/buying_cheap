import re

from main.crawlers.main import Main

from bs4 import BeautifulSoup


class Bikeinn(Main):

    store = "Bikeinn"
    url_base = "https://www.bikeinn.com"
    url_domain_https = "https://www.bikeinn.com/loja-ciclismo"
    url_domain_http = "https://www.bikeinn.com/loja-ciclismo"

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
            price = self._extract_price()
            if price:
                price = re.sub(r' *R\$', '', price)
                price = float(price.strip())
            self._price = price
        return self._price

    @property
    def image(self):
        if not hasattr(self, "_image"):
            self._image = self._extract_url_image()
        return self._image

    @property
    def avaliable_sizes(self):
        if not hasattr(self, "_avaliable_sizes"):
            self._avaliable_sizes = self._extract_avaliable_sizes()
        return self._avaliable_sizes

    @property
    def description(self):
        if not hasattr(self, "_description"):
            self._description = self._extract_description()
        return self._description

    def _extract_price(self):
        try:
            price = self.result.find('div', id='datos_producto_precio').p.text
        except Exception:
            price = None
        return price

    def _extract_url_image(self):
        try:
            url_image = self.result.find("div", id="bigImg").img.get("src")
            url_image = self.url_base + url_image
        except Exception:
            url_image = None
        return url_image

    def _extract_avaliable_sizes(self):
        try:
            sizes = [size.string for size in self.result.find('select', id='tallas_detalle').find_all('option')]
        except Exception:
            sizes = []
        return sizes

    def _extract_description(self):
        try:
            description = self.result.find("span", id="desc").text
            description = re.search("^\s*(?P<description>[\w\s\.,]+)\.\s*$", description).group("description")
        except Exception:
            description = None
        return description

    def _extract_page(self):
        return super()._request_page(self.url)

    def _extract_result(self):
        return BeautifulSoup(self.page, "html.parser")
