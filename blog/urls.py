from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^wines/(?P<pk>\d+)/$', views.wine_detail, name='wine_detail'),
    url(r'^wines/(?P<pk>\d+)/edit/$', views.edit_wine, name='edit_wine'),
    url(r'^wines/new/$', views.new_wine, name='new_wine'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.delete_wine, name='delete_wine'),
]




# url(r'^wines/(?P<pk>\d+)/(?P<im>.+)/rotate/$', views.rotate_image, name='rotate_image'),