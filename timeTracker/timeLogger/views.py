# Create your views here.
from timeLogger.models import logActivity
from timeLogger.forms import logActivityForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

def showLogs(request):
    logs = logActivity.objects.all()
    context = {'logs': logs}
    return render(request, 'index.html', context)

def addLog(request):
    if request.method == 'GET':
        form = logActivityForm()
        return render(request,'form.html',locals())
    elif request.method == 'POST':
        form = logActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs')
        else:
            return redirect('logs')

def delLog(request, logId):
    logs = logActivity.objects.filter(id=logId).delete()
    return redirect('logs')

