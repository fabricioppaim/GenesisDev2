from django.urls import path
from . import views

app_name = 'webs'

urlpatterns = [
    path('', views.WebListView.as_view(), name='web_list'),
    path('<int:pk>/', views.WebDetailView.as_view(), name='detalhe'),
    path('novo/', views.WebCreateView.as_view(), name='novo'),
    path('<int:pk>/editar/', views.WebUpdateView.as_view(), name='editar'),
]
