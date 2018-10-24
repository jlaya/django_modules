from django.conf.urls import url
from .views import LoginView
from .views import LogoutView
from .views import SingupView


urlpatterns = [
               url(r'^login/$', LoginView.as_view(), name='view_login'),
               url(r'^logout/$', LogoutView.as_view(), name='view_logout'),
               url(r'^singup/$', SingupView.as_view(), name='view_singup'),               
               ]