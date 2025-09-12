from django.urls import path
from . import views

app_name = 'bancodedados'

urlpatterns = [
    path('', views.BancoDeDadosListView.as_view(), name='bancodedados_list'),
    path('<int:pk>/', views.BancoDeDadosDetailView.as_view(), name='detalhe'),
    path('novo/', views.BancoDeDadosCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.BancoDeDadosUpdateView.as_view(), name='editar'),
]
