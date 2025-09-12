
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import Projeto

class DashboardView(TemplateView):
    template_name = 'projetos/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        return context

class ProjetoListView(ListView):
    model = Projeto
    template_name = 'projetos/projeto_list.html'

class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = 'projetos/projeto_detail.html'

class ProjetoCreateView(CreateView):
    model = Projeto
    fields = ['name', 'version', 'server_kb_alias', 'kb_version', 'target_path', 'arquivos_complementares', 'exclude_files', 'directory_config_msbuild', 'base_gam', 'https']
    template_name = 'projetos/projeto_form.html'

class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = ['name', 'version', 'server_kb_alias', 'kb_version', 'target_path', 'arquivos_complementares', 'exclude_files', 'directory_config_msbuild', 'base_gam', 'https']
    template_name = 'projetos/projeto_form.html'
