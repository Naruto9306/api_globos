"""
URL configuration for bgglobos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from globos.views import *
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^correos$', CorreoLista.as_view()), 
    re_path(r'correos/(?P<pk>[0-9]*)$', CorreoDetalles.as_view()),
    re_path(r'^personas$', PersonasLista.as_view()), 
    re_path(r'personas/(?P<pk>[0-9]*)$', PersonasDetalles.as_view()),
    re_path(r'^pais$', PaisLista.as_view()), 
    re_path(r'pais/(?P<pk>[0-9]*)$', PaisDetalles.as_view()),
    re_path(r'^provincia$', ProvinciaLista.as_view()), 
    re_path(r'provincia/(?P<pk>[0-9]*)$', ProvinciaDetalles.as_view()),
    re_path(r'^municipio$', MunicipioLista.as_view()), 
    re_path(r'municipio/(?P<pk>[0-9]*)$', MunicipioDetalles.as_view()),
    re_path(r'^producto$', ProductoLista.as_view()), 
    re_path(r'producto/(?P<pk>[0-9]*)$', ProductoDetalles.as_view()),
    re_path(r'^base$', BaseLista.as_view()), 
    re_path(r'base/(?P<pk>[0-9]*)$', BaseDetalles.as_view()),
    re_path(r'^arco$', ArcoLista.as_view()), 
    re_path(r'arco/(?P<pk>[0-9]*)$', ArcoDetalles.as_view()),
    re_path(r'^centromesa$', CentromesaLista.as_view()), 
    re_path(r'centromesa/(?P<pk>[0-9]*)$', CentromesaDetalles.as_view()),
    re_path(r'^cubiertos$', CubiertosLista.as_view()), 
    re_path(r'cubiertos/(?P<pk>[0-9]*)$', CubiertosDetalles.as_view()),
    re_path(r'^mes$', MesLista.as_view()), 
    re_path(r'mes/(?P<pk>[0-9]*)$', MesDetalles.as_view()),
    # re_path(r'^cartel$', CartelLista.as_view()), 
    # re_path(r'cartel/(?P<pk>[0-9]*)$', CartelDetalles.as_view()),
    re_path(r'^contrato$', ContratoLista.as_view()), 
    re_path(r'contrato/(?P<pk>[0-9]*)$', ContratoDetalles.as_view()),
    re_path(r'^globos$', GlobosLista.as_view()), 
    re_path(r'globos/(?P<pk>[0-9]*)$', GlobosDetalles.as_view()),
    re_path(r'^pinata$', PinataLista.as_view()), 
    re_path(r'pinata/(?P<pk>[0-9]*)$', PinataDetalles.as_view()),
    re_path(r'^evento$', EventoLista.as_view()), 
    re_path(r'evento/(?P<pk>[0-9]*)$', EventoDetalles.as_view()),
    re_path(r'^combo$', ComboLista.as_view()), 
    re_path(r'combo/(?P<pk>[0-9]*)$', ComboDetalles.as_view()),
    re_path(r'^tematica$', TematicaLista.as_view()), 
    re_path(r'tematica/(?P<pk>[0-9]*)$', TematicaDetalles.as_view()),
    re_path(r'^cubierto$', CubiertosLista.as_view()), 
    re_path(r'cubierto/(?P<pk>[0-9]*)$', CubiertosDetalles.as_view()),
    # path('enviar_mensaje/', EmailApiView.as_view(), name='send_email')
    # path(r'correos?direccion=$', CorreoDetalles.as_view()),
    # path('', include('globos.urls'))
]
