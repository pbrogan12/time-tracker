from django.conf.urls import patterns, url
from timeLogger import views

urlpatterns =  patterns('',
        url(r'^$',views.showLogs, name='logs'),
        url(r'add/log$', views.addLog, name='addLog'),
        url(r'add/activity$', views.addActivity, name='addActivity'),
        url(r'activities/$', views.showActivities, name='showActivities'),
        url(r'remove/(\d+)/$', views.delLog, name='delLog'),

)

