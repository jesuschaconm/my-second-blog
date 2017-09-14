from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list ,name = "home"),
        url(r'^agregar/$', views.post_agregar,name = 'agregar'),
        url(r'^editar/(?P<pk>[0-9]+)/$', views.post_editar,name = 'editar'),
        url(r'^eliminar/(?P<pk>[0-9]+)/$', views.post_eliminar,name = 'eliminar'),
    ]