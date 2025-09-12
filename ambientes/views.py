from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Ambiente

class AmbienteListView(ListView):
    model = Ambiente
    template_name = 'ambientes/ambiente_list.html'

class AmbienteDetailView(DetailView):
    model = Ambiente
    template_name = 'ambientes/ambiente_detail.html'

class AmbienteCreateView(CreateView):
    model = Ambiente
    fields = ['name', 'sufixo', 'ativo']
    template_name = 'ambientes/ambiente_form.html'

class AmbienteUpdateView(UpdateView):
    model = Ambiente
    fields = ['name', 'sufixo', 'ativo']
    template_name = 'ambientes/ambiente_form.html'
