from django.urls import path
from . import views

app_name = 'empresas'

urlpatterns = [
    path('', views.EmpresaListView.as_view(), name='empresa_list'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='detalhe'),
    path('novo/', views.EmpresaCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.EmpresaUpdateView.as_view(), name='editar'),
]
