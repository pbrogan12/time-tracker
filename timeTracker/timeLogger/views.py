# Create your views here.
from django.db.models import Sum
from timeLogger.models import logActivity, Activity
from timeLogger.forms import LogActivityForm, ActivityForm
from accounts.models import MyProfile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime 

@login_required(login_url='/accounts/signin')
def showLogs(request):
    if request.method == 'GET':
        logs = logActivity.objects.filter(date=datetime.date.today())
        totalTime = logActivity.objects.filter(date=datetime.date.today()).aggregate(Sum('time'))
        totalTime = totalTime['time__sum']
        form = LogActivityForm()
        return render(request,'log.html',locals())
    elif request.method == 'POST':
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = logActivity(account_id=accountId.id)
        postValues = request.POST.copy()
        b = postValues['time'].split(':')
        time = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])
        postValues['time'] = time
        form = LogActivityForm(postValues, instance=form)
        if form.is_valid():
            form.save()
            return redirect('logs')
        else:
            logs = logActivity.objects.filter(date=datetime.date.today())
            return render(request,'log.html',locals())

def showLogsLast7(request):
    dateRange = datetime.date.today()-datetime.timedelta(days=7)
    logs = logActivity.objects.filter(date__gte=dateRange).order_by('-date')
    totalTime = logActivity.objects.filter(date__gte=dateRange).aggregate(Sum('time'))
    totalTime = totalTime['time__sum']
    return render(request,'detailedLog.html',locals())

def showActivities(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        context = {'activities':activities}
        form = ActivityForm()
        return render(request,'activities.html',locals())
    elif request.method == 'POST':
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = Activity(account_id=accountId.id)
        form = ActivityForm(request.POST, instance=form)
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
        postValues = request.POST.copy()
        b = postValues['time'].split(':')
        time = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])
        postValues['time'] = time
        form = LogActivityForm(postValues, instance=logs)
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
