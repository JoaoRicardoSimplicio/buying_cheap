from main.models import Store

from tqdm import tqdm


list_stores = [
    'Kabum',
    'Shop2gether',
    'Netshoes'
]


def register():
    for store in tqdm(list_stores):
        store, _ = Store.objects.get_or_create(name=store)
