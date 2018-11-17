from django.conf.urls import url
from .views import CreateInvoice
from .views import UpdateInvoice


urlpatterns = [
                #url(r'^inlineform/list/$', ChartList.as_view(), name='chartlist_view'),
				#url(r'^inlineform/Detail/(?P<pk>[0-9]+)/$', ChartDetail.as_view(), name='chartdetail_view'),
				url(r'^inlineform/create/$', CreateInvoice.as_view(), name='invoice_create_view'),
			    #url(r'^inlineform/Detail/$', plot, name='chartdetail_view'),
                url(r'^inlineform/update/(?P<pk>[0-9]+)/$', UpdateInvoice.as_view(), name='invoice_cupdate_course'),
              ]