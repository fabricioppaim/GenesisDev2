from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import LogGenexus

class LogGenexusListView(ListView):
    model = LogGenexus
    template_name = 'loggenexus/loggenexus_list.html'

class LogGenexusDetailView(DetailView):
    model = LogGenexus
    template_name = 'loggenexus/loggenexus_detail.html'

class LogGenexusCreateView(CreateView):
    model = LogGenexus
    fields = ['conversion_pattern', 'ambientes']
    template_name = 'loggenexus/loggenexus_form.html'

class LogGenexusUpdateView(UpdateView):
    model = LogGenexus
    fields = ['conversion_pattern', 'ambientes']
    template_name = 'loggenexus/loggenexus_form.html'
