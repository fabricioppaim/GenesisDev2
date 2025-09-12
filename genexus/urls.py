from django.urls import path
from . import views

app_name = 'genexus'

urlpatterns = [
    path('', views.GenexusListView.as_view(), name='genexus_list'),
    path('<int:pk>/', views.GenexusDetailView.as_view(), name='detalhe'),
    path('novo/', views.GenexusCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.GenexusUpdateView.as_view(), name='editar'),
]
