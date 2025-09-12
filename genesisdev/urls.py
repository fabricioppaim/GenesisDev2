"""
URL configuration for genesisdev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from django.urls import include, path
from projetos.views import DashboardView

from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('ambientes/', include(('ambientes.urls', 'ambientes'), namespace='ambientes')),
    path('empresas/', include(('empresas.urls', 'empresas'), namespace='empresas')),
    path('projetos/', include(('projetos.urls', 'projetos'), namespace='projetos')),
    path('bancodedados/', include(('bancodedados.urls', 'bancodedados'), namespace='bancodedados')),
    path('webs/', include(('webs.urls', 'webs'), namespace='webs')),
    path('gams/', include(('gams.urls', 'gams'), namespace='gams')),
    path('loggenexus/', include(('loggenexus.urls', 'loggenexus'), namespace='loggenexus')),
    path('genexus/', include(('genexus.urls', 'genexus'), namespace='genexus')),
    path('credenciais/', include(('credenciais.urls', 'credenciais'), namespace='credenciais')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, "static"))
    urlpatterns += static('/admin-interface/', document_root=os.path.join(settings.BASE_DIR, "admin-interface"))