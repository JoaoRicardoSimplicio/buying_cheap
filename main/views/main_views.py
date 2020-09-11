from django.views.generic import ListView

from main.models import Store


class Home(ListView):

    model = Store
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
