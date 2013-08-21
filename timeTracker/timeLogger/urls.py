from django.conf.urls import patterns, url
from timeLogger import views

urlpatterns =  patterns('',
        url(r'^$',views.showLogs, name='logs'),
        url(r'add/$', views.addLog, name='addLog'),
        url(r'remove/(\d+)/$', views.delLog, name='delLog'),

)

