from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login$', views.login_view, name='login'),
    url(r'^login_result$', views.login_result_view, name='login_result'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^pairholders$', views.list_view_pairholders, name='list_view_pairholders'),
    url(r'^(?P<my_model_id>[0-9]+)/$', views.detail_view, name='list_view'),
]
