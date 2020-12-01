from django.core.management.base import BaseCommand, CommandError

import time

from main.models import Product, PriceHistory
from main.services.product import select_store

from tqdm import tqdm


class Command(BaseCommand):
        
    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in tqdm(products):
            self.update_price(product.id)
            time.sleep(10)


    def update_price(self, id):
        try:
            product = Product.objects.get(id=id)
            crawler = select_store(product.store.name)

            PriceHistory.objects.create(
                product=product,
                price_product=product.price_product
            )

            new_information_product = crawler(product.url_product)

            new_product, _ = Product.objects.update_or_create(
                url_product=new_information_product.url,
                defaults={
                    'name': new_information_product.name,
                    'store': product.store,
                    'price_product': new_information_product.price,
                    'description': new_information_product.description
                }
            )
        except Exception as Error:
            print(Error, f"with product {product.url_product}")

