from django.conf.urls import url
from .views import DetailCourse
from .views import ListCourse
from .views import CreateCourse
from .views import UpdateCourse
from .views import DeleteCourse


urlpatterns = [
               url(r'^Course/list$', ListCourse.as_view(),
                   name='list_course'),
               url(r'^Course/Create/$',
                   CreateCourse.as_view(), name='create_course'),
               url(r'^Course/Detail/(?P<pk>[0-9]+)/$',
                   DetailCourse.as_view(), name='detail_course'),
               url(r'^Course/Update/(?P<pk>[0-9]+)/$',
                   UpdateCourse.as_view(), name='update_course'),
               url(r'^Course/Delete/(?P<pk>[0-9]+)/$',
                   DeleteCourse.as_view(), name='delete_course'),
               ]