from django.conf.urls import patterns, url
from timeLogger import views

urlpatterns =  patterns('',
        url(r'^$', views.showLogs, name='logs'),
        url(r'last7/$', views.showLogsLast7, name='logsLast7'),
        url(r'activities/$', views.showActivities, name='showActivities'),
        url(r'activities/(\d+)/remove$', views.delActivity, name='delActivity'),
        url(r'(\d+)/remove$', views.delLog, name='delLog'),
        url(r'(\d+)/edit$', views.editLog, name='editLog'),

)

