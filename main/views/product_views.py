from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from django.contrib import messages

from main.forms import ProductForm
from main.services.product import ProductTool
from main.services.store import verify_if_store_exists
from main.models import Product, Store
from main.queries.product_queries import product_ordination


class ProductCreate(View):

    def post(self, request, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                product = ProductTool()
                product.create(request.POST)
                return HttpResponseRedirect(reverse('product_list'))
            except Exception as Error:
                messages.error(request, Error)
                return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(
                request, "Certifique de digitar uma url correta e escolher a loja correspondente"
            )
            return HttpResponseRedirect(reverse("index"))


class ProductList(ListView):

    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stores"] = Store.objects.all()
        return context

    def get_queryset(self):
        store = self.request.GET.get("store")
        if verify_if_store_exists(store):
            products = Product.objects.filter(store__name=store)
        else:
            products = Product.objects.all()
        products = product_ordination(products)
        return products


class ProductDetail(DetailView):

    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
