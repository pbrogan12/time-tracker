# Create your views here.
from timeLogger.models import logActivity, Activity
from timeLogger.forms import LogActivityForm, ActivityForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

def showLogs(request):
    if request.method == 'GET':
        logs = logActivity.objects.all()
        context = {'logs': logs}
        form = LogActivityForm()
        return render(request,'log.html',locals())
    elif request.method == 'POST':
        form = LogActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs')
        else:
            return redirect('logs')


def showActivities(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        context = {'activities':activities}
        form = ActivityForm()
        return render(request,'activities.html',locals())
    elif request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showActivities')
        else:
            return redirect('showActivities')

def delLog(request, logId):
    logs = logActivity.objects.filter(id=logId).delete()
    return redirect('logs')

def delActivity(request, logId):
    logs = Activity.objects.filter(id=logId).delete()
    return redirect('showActivities')
