from django.contrib import admin
from timeLogger.models import Activity, logActivity, dailySummary

admin.site.register(Activity)
admin.site.register(logActivity)
admin.site.register(dailySummary)
