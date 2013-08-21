from django.conf.urls import patterns, url
from timeLogger import views

urlpatterns =  patterns('',
        url(r'^$',views.showLogs, name='logs')
)

