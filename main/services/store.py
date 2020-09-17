from main.models import Store

def verify_if_store_exists(name):
    if Store.objects.filter(name=name).exists():
        return True
    else:
        return False