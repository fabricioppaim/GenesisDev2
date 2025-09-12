from django.urls import path
from . import views

app_name = 'ambientes'

urlpatterns = [
    path('', views.AmbienteListView.as_view(), name='ambiente_list'),
    path('<int:pk>/', views.AmbienteDetailView.as_view(), name='detalhe'),
    path('novo/', views.AmbienteCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.AmbienteUpdateView.as_view(), name='editar'),
]
