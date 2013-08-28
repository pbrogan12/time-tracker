from django.forms import ModelForm
from timeLogger.views import logActivity, Activity

class LogActivityForm(ModelForm):
    class Meta:
        model = logActivity
        exclude = ('account',)

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ('account',)
