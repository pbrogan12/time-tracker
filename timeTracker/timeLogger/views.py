# Create your views here.
from django.db.models import Sum
from timeLogger.models import logActivity, Activity
from timeLogger.forms import LogActivityForm, ActivityForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

def showLogs(request):
    if request.method == 'GET':
        logs = logActivity.objects.all()
        totalTime = logActivity.objects.aggregate(Sum('time'))
        totalTime = totalTime['time__sum']
        form = LogActivityForm()
        return render(request,'log.html',locals())
    elif request.method == 'POST':
        postValues = request.POST.copy()
        b = postValues['time'].split(':')
        time = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])
        postValues['time'] = time
        form = LogActivityForm(postValues)
        if form.is_valid():
            form.save()
            return redirect('logs')
        else:
            logs = logActivity.objects.all()
            return render(request,'log.html',locals())


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
            activities = Activity.objects.all()
            return render(request,'activities.html',locals())
def editLog(request, logId):
    logs = logActivity.objects.get(id=logId)
    if request.method == 'GET':
        form = LogActivityForm(instance=logs)
        return render(request,'form.html',locals())
    elif request.method == 'POST':
        form = LogActivityForm(request.POST, instance=logs)
        if form.is_valid():
            form.save()
            return redirect('logs')
        else:
            form = LogActivityForm(instance=logs)
            return render(request,'form.html',locals())

def delLog(request, logId):
    logs = logActivity.objects.filter(id=logId).delete()
    return redirect('logs')

def delActivity(request, logId):
    logs = Activity.objects.filter(id=logId).delete()
    return redirect('showActivities')
