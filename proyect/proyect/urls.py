"""proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from proyect.views import cambiarnombre, index, index2, test, atras, abrir, crear, cambiarnombre, eliminar, copiar, cortar, pegar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('test/', test),
    path('index2/<Porta>/<Ruta>/', index2),
    path('crear/<Porta>/<Ruta>/', crear),
    path('abrir/<Porta>/<Ruta>/', abrir),
    path('atras/<Porta>/<Ruta>/', atras),
    path('cambiarnombre/<Porta>/<Ruta>/', cambiarnombre),
    path('eliminar/<Porta>/<Ruta>/', eliminar),
    path('copiar/<Porta>/<Ruta>/', copiar),
    path('cortar/<Porta>/<Ruta>/', cortar),
    path('pegar/<Porta>/<Ruta>/', pegar),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
