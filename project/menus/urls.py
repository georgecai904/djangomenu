from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.show_menus, name='index'),
    url('^menus/(?P<menu_id>[0-9]+)/$', views.show_menu),
]
