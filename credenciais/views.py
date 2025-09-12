from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Credencial

class CredencialListView(ListView):
    model = Credencial
    template_name = 'credenciais/credencial_list.html'

class CredencialDetailView(DetailView):
    model = Credencial
    template_name = 'credenciais/credencial_detail.html'

class CredencialCreateView(CreateView):
    model = Credencial
    fields = ['name', 'cred_id']
    template_name = 'credenciais/credencial_form.html'

class CredencialUpdateView(UpdateView):
    model = Credencial
    fields = ['name', 'cred_id']
    template_name = 'credenciais/credencial_form.html'
