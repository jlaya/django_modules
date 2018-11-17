from django.conf.urls import url
from .views import CreateInvoice
from .views import UpdateInvoice


urlpatterns = [
                url(r'^Chart/list/$', ChartList.as_view(), name='chartlist_view'),
				url(r'^Chart/Detail/(?P<pk>[0-9]+)/$', ChartDetail.as_view(), name='chartdetail_view'),
				url(r'^Chart/Create/$', ChartCreate.as_view(), name='chartcreate_view'),
			    #url(r'^Chart/Detail/$', plot, name='chartdetail_view'),

              ]