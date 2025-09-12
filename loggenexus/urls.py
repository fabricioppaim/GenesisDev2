from django.urls import path
from . import views

app_name = 'loggenexus'

urlpatterns = [
    path('', views.LogGenexusListView.as_view(), name='loggenexus_list'),
    path('<int:pk>/', views.LogGenexusDetailView.as_view(), name='detalhe'),
    path('novo/', views.LogGenexusCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.LogGenexusUpdateView.as_view(), name='editar'),
]
