from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import GAM

class GAMListView(ListView):
    model = GAM
    template_name = 'gams/gam_list.html'

class GAMDetailView(DetailView):
    model = GAM
    template_name = 'gams/gam_detail.html'

class GAMCreateView(CreateView):
    model = GAM
    fields = ['user_id_gam_admin', 'user_id_gam_connection', 'ambientes']
    template_name = 'gams/gam_form.html'

class GAMUpdateView(UpdateView):
    model = GAM
    fields = ['user_id_gam_admin', 'user_id_gam_connection', 'ambientes']
    template_name = 'gams/gam_form.html'
