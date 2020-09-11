from main.crawlers.shop2gether import StoreShop2gether
from main.crawlers.kabum import StoreKabum
from main.crawlers.netshoes import StoreNetshoes

from main.models import Product, Store


class ProductTool:

    def __init__(self):
        pass

    def create(self, *args, **kwargs):
        for item in args:
            store_name = select_store(item['name'])
            try:
                store_crawler = store_name(item['url_product'])
                store, _ = Store.objects.get_or_create(
                    name=store_crawler.store
                )
                product, _ = Product.objects.update_or_create(
                    url_product=store_crawler.url,
                    defaults={
                        'name': store_crawler.name,
                        'store': store,
                        'price_product': store_crawler.price,
                        'description_product': store_crawler.description,
                        'url_image': store_crawler.image
                    }
                )
            except Exception as Error:
                raise Error


def select_store(name):
    if name == "Shop2gether":
        return StoreShop2gether
    elif name == "Kabum":
        return StoreKabum
    elif name == "Netshoes":
        return StoreNetshoes
