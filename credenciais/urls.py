from django.urls import path
from . import views

app_name = 'credenciais'

urlpatterns = [
    path('', views.CredencialListView.as_view(), name='credencial_list'),
    path('<int:pk>/', views.CredencialDetailView.as_view(), name='detalhe'),
    path('novo/', views.CredencialCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.CredencialUpdateView.as_view(), name='editar'),
]
