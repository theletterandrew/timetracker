from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manager, name = 'manager'),
    url(r'^addproject/$', views.add, name = 'add')
]
