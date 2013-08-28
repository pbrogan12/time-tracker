from django.db import models
from accounts.models import MyProfile
# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=20)
    account = models.ForeignKey(MyProfile)

    def __unicode__(self):
        return self.name

class logActivity(models.Model):
    name = models.ForeignKey('Activity')
    date = models.DateField()
    time = models.IntegerField()
    notes = models.TextField()
    account = models.ForeignKey(MyProfile)
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.notes)
