from django.forms import ModelForm
from timeLogger.views import logActivity, Activity, dailySummary

class dailySummaryForm(ModelForm):
    class Meta:
        model = dailySummary

class LogActivityForm(ModelForm):
    class Meta:
        model = logActivity
        exclude = ('account','date','name',)

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ('account',)
