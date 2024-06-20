from django.urls import path, re_path
# from django.conf.urls import url

from . import views

urlpatterns = [
   path(r'^correos$', views.CorreoLista.as_view()), 
   path(r'correos/(?P<pk>[0-9]*)$', views.CorreoDetalles.as_view()),
]