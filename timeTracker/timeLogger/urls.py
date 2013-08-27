from django.conf.urls import patterns, url
from timeLogger import views

urlpatterns =  patterns('',
        url(r'^$', views.showLogs, name='logs'),
        url(r'activities/$', views.showActivities, name='showActivities'),
        url(r'remove/(\d+)/log$', views.delLog, name='delLog'),
        url(r'remove/(\d+)/activity$', views.delActivity, name='delActivity'),
        url(r'(\d+)/edit$', views.editLog, name='editLog'),

)

