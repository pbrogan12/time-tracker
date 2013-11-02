# Create your views here.
from django.db.models import Sum
from timeLogger.models import logActivity, Activity, dailySummary
from timeLogger.forms import LogActivityForm, ActivityForm, dailySummaryForm
from accounts.models import MyProfile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='/accounts/signin')
def addLog(request, actId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    activityName = Activity.objects.get(account_id=accountId.id,id=actId)
    if activityName:
        log = logActivity(account_id=accountId.id,name_id=activityName.id)
        f = logActivity.objects.create(date=datetime.date.today(),time= 0,account_id=accountId.id,name_id=activityName.id)
        f.save()
        return redirect('editLog',f.id)
    else:
        return redirect('logs')

@login_required(login_url='/accounts/signin')
def showTodaysLogs(request):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    activities = Activity.objects.filter(account_id=accountId.id)
    print activities
    logs = logActivity.objects.filter(date=datetime.date.today(),account_id=accountId.id)
    totalTime = logActivity.objects.filter(date=datetime.date.today(),account_id=accountId.id).aggregate(Sum('time'))
    totalTime = totalTime['time__sum']
    return render(request,'log.html',locals())

@login_required(login_url='/accounts/signin')
def showLast7Logs(request):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    dateRange = datetime.date.today()-datetime.timedelta(days=7)
    logs = logActivity.objects.filter(date__gte=dateRange,account_id=accountId.id).order_by('-date')
    totalTime = logActivity.objects.filter(date__gte=dateRange,account_id=accountId.id).aggregate(Sum('time'))
    totalTime = totalTime['time__sum']
    return render(request,'detailedLog.html',locals())

@login_required(login_url='/accounts/signin')
def showAllLogs(request):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    logs = logActivity.objects.filter(account_id=accountId.id)
    totalTime = logActivity.objects.filter(account_id=accountId.id).aggregate(Sum('time'))
    totalTime = totalTime['time__sum']
    return render(request,'allLogs.html',locals())

@login_required(login_url='/accounts/signin')
def showActivities(request):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    if request.method == 'GET':
        activities = Activity.objects.filter(account_id=accountId.id)
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
            activities = Activity.objects.filter(account_id=accountId.id)
            return render(request,'activities.html',locals())

@login_required(login_url='/accounts/signin')
def editLog(request, logId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    logs = logActivity.objects.get(account_id=accountId.id, id=logId)
    if request.method == 'GET':
        form = LogActivityForm(instance=logs)
        return render(request,'form.html',locals())
    elif request.method == 'POST':
        postValues = request.POST.copy()
        try:
            b = postValues['time'].split(':')
            time = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])
            postValues['time'] = time
        except:
            pass
        form = LogActivityForm(postValues, instance=logs)
        if form.is_valid():
            form.save()
            if dailySummary.objects.filter(account_id=accountId.id,date=datetime.date.today()).exists():
                pass
            else:
                data = {'date' : datetime.date.today(),
                        'account' : accountId.id,
                        'rating' : ''}
                f = dailySummaryForm(data)
                if f.is_valid():
                    f.save()
                else:
                    pass
            return redirect('logs')
        else:
            form.errors['time'] = "Format must be in HH:MM:SS"
            return render(request,'form.html',locals())

@login_required(login_url='/accounts/signin')
def delLog(request, logId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    logActivity.objects.get(account_id=accountId.id,id=logId).delete()
    return redirect('logs')

@login_required(login_url='/accounts/signin')
def delActivity(request, logId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    Activity.objects.get(account_id=accountId.id,id=logId).delete()
    return redirect('showActivities')

