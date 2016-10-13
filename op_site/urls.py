#! coding:utf-8
"""op_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from op_app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', logout, name='logout'),

    url(r'^idc_list/$', idc_list, name='idc_list'),
    url(r'^idc_add/$', idc_add, name='idc_add'),
    url(r'^idc_update/$', idc_update, name='idc_update'),
    url(r'^idc_delete/$', idc_delete, name='idc_delete'),

    url(r'^server_list/$', server_list, name='server_list'),
    url(r'^server_update/$', server_update, name='server_update'),
    url(r'^server_detail/$', server_detail, name='server_detail'),
    url(r'^server_delete/$', server_delete, name='server_delete'),
    url(r'^server_add/$', server_add, name='server_add'),

    url(r'^app_list/$', app_list, name='app_list'),
    url(r'^app_delete/$', app_delete, name='app_delete'),
    url(r'^app_update/$', app_update, name='app_update'),
    url(r'^app_add/$', app_add, name='app_add'),

    url(r'^hostaccount_list/$', hostaccount_list, name='hostaccount_list'),
    url(r'^hostaccount_update/$', hostaccount_update, name='hostaccount_update'),
    url(r'^hostaccount_delete/$', hostaccount_delete, name='hostaccount_delete'),
    url(r'^hostaccount_add/$', hostaccount_add, name='hostaccount_add'),

    url(r'^tcpdump_list/$', tcpdump_list, name='tcpdump_list'),
    url(r'^tcpdump_start/$', tcpdump_start, name='tcpdump_start'),
    url(r'^tcpdump_stop/$', tcpdump_stop, name='tcpdump_stop'),
    url(r'^tcpdump_update/$', tcpdump_update, name='tcpdump_update'),
    url(r'^tcpdump_delete/$', tcpdump_delete, name='tcpdump_delete'),
    url(r'^tcpdump_add/$', tcpdump_add, name='tcpdump_add'),

    url(r'^app_status_list/$', app_status_list, name='app_status_list'),
    url(r'^api_status_list/$', api_status_list, name='api_status_list'),

    url(r'^up_load_list/$', up_load_list, name='up_load_list'),
    url(r'^upload_file/$', upload_file, name='upload_file'),

    url(r'^app_package_list/$', app_package_list, name='app_package_list'),

    url(r'^exec_command/$', exec_command, name='exec_command'),
]

