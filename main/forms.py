from django import forms

from main.models import Product


class ProductForm(forms.Form):
    url_product = forms.URLField(max_length=500)
    name = forms.CharField(max_length=100)

    class Meta:
        model = Product
        fields = [
            "name", "store", "url_product", "id_product_store", "price_product", "description_product"
        ]
