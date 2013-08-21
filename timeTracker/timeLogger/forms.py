from django.forms import ModelForm
from timeLogger.views import logActivity

class logActivityForm(ModelForm):
    class Meta:
        model = logActivity
