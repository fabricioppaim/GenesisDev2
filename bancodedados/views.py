from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BancoDeDados, BancoDados

class BancoDeDadosListView(ListView):
    model = BancoDeDados
    template_name = 'bancodedados/bancodedados_list.html'

class BancoDeDadosDetailView(DetailView):
    model = BancoDeDados
    template_name = 'bancodedados/bancodedados_detail.html'

class BancoDeDadosCreateView(CreateView):
    model = BancoDeDados
    fields = ['name', 'service_name', 'engine', 'ambientes']
    template_name = 'bancodedados/bancodedados_form.html'

class BancoDeDadosUpdateView(UpdateView):
    model = BancoDeDados
    fields = ['name', 'service_name', 'engine', 'ambientes']
    template_name = 'bancodedados/bancodedados_form.html'

class BancoDadosDetailView(DetailView):
    model = BancoDados
    template_name = 'bancodedados/bancodados_detail.html'
