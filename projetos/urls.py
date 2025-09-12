from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.ProjetoListView.as_view(), name='projeto_list'),
    path('<int:pk>/', views.ProjetoDetailView.as_view(), name='detalhe'),
    path('novo/', views.ProjetoCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='editar'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
