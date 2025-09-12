from django.urls import path
from . import views

app_name = 'gams'

urlpatterns = [
    path('', views.GAMListView.as_view(), name='gam_list'),
    path('<int:pk>/', views.GAMDetailView.as_view(), name='detalhe'),
    path('novo/', views.GAMCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.GAMUpdateView.as_view(), name='editar'),
]
