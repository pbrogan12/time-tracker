# Create your views here.
from timeLogger.models import logActivity, Activity
from timeLogger.forms import LogActivityForm, ActivityForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

def showLogs(request):
    logs = logActivity.objects.all()
    context = {'logs': logs}
    return render(request, 'log.html', context)

def showActivities(request):
    activities = Activity.objects.all()
    context = {'activities':activities}
    return render(request, 'activities.html', context)

def addLog(request):
    if request.method == 'GET':
        form = LogActivityForm()
        return render(request,'form.html',locals())
    elif request.method == 'POST':
        form = LogActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs')
        else:
            return redirect('logs')

def addActivity(request):
    if request.method == 'GET':
        form = ActivityForm()
        return render(request,'form.html',locals())
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
