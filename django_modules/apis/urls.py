from django.conf.urls import url, include
from .views import ProductsListAPI
from .views import ProductsDetailAPI
from .views import ProductsCreateAPI
from .views import ProductsUpdateAPI
from .views import ProductsDeleteAPI


urlpatterns = [
               url(r'^productlist/$', ProductsListAPI.as_view()),
               url(r'^product/create/$', ProductsCreateAPI.as_view()),
               url(r'^product/detail/(?P<pk>[0-9]+)/$', ProductsDetailAPI.as_view()),
               url(r'^product/update/(?P<pk>[0-9]+)/$', ProductsUpdateAPI.as_view()),
               url(r'^product/delete/(?P<pk>[0-9]+)/$', ProductsDeleteAPI.as_view()),
               ]