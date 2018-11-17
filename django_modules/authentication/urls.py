from django.conf.urls import url
from .views import LoginView
from .views import LogoutView
from .views import SingupView
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
               url(r'^login/$', LoginView.as_view(), name='view_login'),
               url(r'^logout/$', LogoutView.as_view(), name='view_logout'),
               url(r'^singup/$', SingupView.as_view(), name='view_singup'),

			   url(r'^reset/password/reset/$', password_reset, {'template_name': 'authentication/password_reset_form.html', 'email_template_name': 'authentication/password_reset_email.html'}, name='password_reset'),
			   url(r'^reset/password/reset/done/$', password_reset_done, {'template_name': 'authentication/password_reset_done.html'}, name='password_reset_done'),
			   url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'authentication/password_reset_confirm.html'}, name='password_reset_confirm'),
			   url(r'^reset/done/$', password_reset_complete, {'template_name': 'authentication/password_reset_complete.html'}, name='password_reset_complete'),
               ]