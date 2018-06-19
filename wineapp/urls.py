from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^wines/new/$', views.new_wine, name='new_wine'),
    url(r'^wines/(?P<pk>\d+)/$', views.wine_detail, name='wine_detail'),
    url(r'^wines/(?P<pk>\d+)/edit/$', views.edit_wine, name='edit_wine'),
]