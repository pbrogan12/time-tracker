from django.conf.urls import patterns, url
from timeLogger import views

urlpatterns =  patterns('',
        url(r'^$', views.showTodaysLogs, name='logs'),
        url(r'all/$', views.showAllLogs, name='showAllLogs'),
        url(r'add/(\d+)/$', views.addLog, name='addLog'),
        url(r'last7/$', views.showLast7Logs, name='logsLast7'),
        url(r'activities/$', views.showActivities, name='showActivities'),
        url(r'activities/(\d+)/remove$', views.delActivity, name='delActivity'),
        url(r'(\d+)/remove$', views.delLog, name='delLog'),
        url(r'(\d+)/edit$', views.editLog, name='editLog'),

)

