from django.contrib import admin
from timeLogger.models import Activity, logActivity

admin.site.register(Activity)
admin.site.register(logActivity)
