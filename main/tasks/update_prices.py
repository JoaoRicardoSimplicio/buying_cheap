import time

from main.models import Product, PriceHistory
from main.services.product import select_store

from tqdm import tqdm


def task_update_all_prices():
    products = Product.objects.all()
    for product in tqdm(products):
        update_price(product.id)
        time.sleep(10)


def update_price(id):
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


if __name__ == "__main__":
    task_update_all_prices()
