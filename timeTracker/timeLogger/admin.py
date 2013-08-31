from django.contrib import admin
from timeLogger.models import Activity, logActivity, dailySummary

def username(obj):
    return u'%s' % (obj.account.user)

class dailySummaryAdmin(admin.ModelAdmin):
    list_display = (username,'date','rating')
    ordering = ('rating','-date')

admin.site.register(Activity)
admin.site.register(logActivity)
admin.site.register(dailySummary, dailySummaryAdmin)
