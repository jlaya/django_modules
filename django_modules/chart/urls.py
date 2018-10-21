from django.conf.urls import url
from .views import ChartList
from .views import ChartDetail
from .views import ChartCreate
# from .views import plot


urlpatterns = [
                url(r'^Chart/list/$', ChartList.as_view(), name='chartlist_view'),
				url(r'^Chart/Detail/(?P<pk>[0-9]+)/$', ChartDetail.as_view(), name='chartdetail_view'),
				url(r'^Chart/Create/$', ChartCreate.as_view(), name='chartcreate_view'),
			    #url(r'^Chart/Detail/$', plot, name='chartdetail_view'),

              ]