import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}


class Main:

    def _request_page(self, url):
        try:
            response = requests.get(url, headers=headers)
            return response.content
        except Exception:
            return

    def _request_status_code(self, url):
        try:
            response = requests.get(url, headers=headers)
            return response.status_code
        except Exception:
            return

    def show_attributes(self, product):
        try:
            return dict({
                "name": f"{product.name}",
                "price": f"{product.price}",
                "description": f"{product.description}"
            })
        except KeyError:
            return KeyError
