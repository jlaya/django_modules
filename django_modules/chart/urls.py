from django.conf.urls import url
from .views import ChartList
from .views import ChartDetail


urlpatterns = [
                url(r'^Chart/list/$', ChartList.as_view(), name='chartlist_view'),
				url(r'^Chart/Detail/(?P<pk>[0-9]+)/$', ChartDetail.as_view(), name='chartdetail_view'),
              ]