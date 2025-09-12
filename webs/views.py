from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Web

class WebListView(ListView):
    model = Web
    template_name = 'webs/web_list.html'

class WebDetailView(DetailView):
    model = Web
    template_name = 'webs/web_detail.html'

class WebCreateView(CreateView):
    model = Web
    fields = ['name', 'path', 'shared', 'ambientes', 'finalidade']
    template_name = 'webs/web_form.html'

class WebUpdateView(UpdateView):
    model = Web
    fields = ['name', 'path', 'shared', 'ambientes', 'finalidade']
    template_name = 'webs/web_form.html'
