# Create your views here.
from timeLogger.models import logActivity
from django.http import HttpResponse
from django.shortcuts import render

def showLogs(request):
    logs = logActivity.objects.all()
    context = {'logs': logs}
    return render(request, 'index.html', context)

