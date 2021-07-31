from django.core.management.base import BaseCommand, CommandError

from main.models import Store

from tqdm import tqdm


list_stores = [
    'Kabum',
    'Shop2gether',
    'Netshoes',
    'MercadoLivre',
    'BikePointSC',
    'Zattini',
    'Dafiti',
    'Bikeinn'
]

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for store in tqdm(list_stores):
            try:
                store, _ = Store.objects.get_or_create(name=store)
            except Exception:
                raise Exception(f"Not possible save the store {store}")
