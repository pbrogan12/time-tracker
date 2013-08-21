from django.forms import ModelForm
from timeLogger.views import logActivity, Activity

class LogActivityForm(ModelForm):
    class Meta:
        model = logActivity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
