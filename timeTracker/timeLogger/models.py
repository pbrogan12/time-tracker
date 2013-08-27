from django.db import models
# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class logActivity(models.Model):
    name = models.ForeignKey('Activity')
    date = models.DateField()
    time = models.IntegerField()
    notes = models.TextField()
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.notes)
