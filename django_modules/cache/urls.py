from django.conf.urls import url
from .views import Cache
from django.views.decorators.cache import cache_page


urlpatterns = [
                url(r'^cache/$', Cache.as_view(), name='view_cache'),
                # url(r'^cache/$', cache_page(60 * 5)(Cache.as_view()), name='view_cache'),
              ]
