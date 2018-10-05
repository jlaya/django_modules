from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^sendemail/$', views.send_email, name='view_send_mail'),
]
