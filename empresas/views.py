from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Empresa

class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresas/empresa_list.html'

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresas/empresa_detail.html'

class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['name', 'domain', 'ativo']
    template_name = 'empresas/empresa_form.html'

class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['name', 'domain', 'ativo']
    template_name = 'empresas/empresa_form.html'
