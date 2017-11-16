from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manager, name = 'manager'),
    url(r'^addproject/$', views.add, name = 'add'),
    url(r'^viewproject/(?P<project_id>[0-9]+)/$', views.viewProject, name = 'viewProject'),
]
