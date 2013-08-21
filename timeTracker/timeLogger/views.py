# Create your views here.
from timeLogger.models import logActivity
from django.http import HttpResponse

def showLogs(request):
    a = logActivity.objects.all()
    for i in a:
        print a 
    return HttpResponse(a)

