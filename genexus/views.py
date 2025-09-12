from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Genexus

class GenexusListView(ListView):
    model = Genexus
    template_name = 'genexus/genexus_list.html'

class GenexusDetailView(DetailView):
    model = Genexus
    template_name = 'genexus/genexus_detail.html'

class GenexusCreateView(CreateView):
    model = Genexus
    fields = ['gx_server_url', 'gx_server_version', 'gx_server_working_directory', 'gx_server_working_directory_kb']
    template_name = 'genexus/genexus_form.html'

class GenexusUpdateView(UpdateView):
    model = Genexus
    fields = ['gx_server_url', 'gx_server_version', 'gx_server_working_directory', 'gx_server_working_directory_kb']
    template_name = 'genexus/genexus_form.html'
