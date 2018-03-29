from django.conf.urls import url
from .views import ReportsView
from .views import Wkhtmltopdf


urlpatterns = [
                url(r'^reports/$', ReportsView.as_view(), name='reportsview'),
                url(r'^wkhtmltopdf/$', Wkhtmltopdf.as_view(), name='wkhtmltopdf'),
              ]