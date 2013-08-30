from django.db import models
from accounts.models import MyProfile
# Create your models here.

class dailySummary(models.Model):
    account = models.ForeignKey(MyProfile)
    ratings = (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            )
    date = models.DateField()
    rating = models.CharField(max_length=1, choices=ratings, blank=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.account.user, self.date, self.rating)
    
class Activity(models.Model):
    name = models.CharField(max_length=20)
    account = models.ForeignKey(MyProfile)

    def __unicode__(self):
        return self.name

class logActivity(models.Model):
    name = models.ForeignKey('Activity')
    date = models.DateField()
    time = models.IntegerField()
    notes = models.TextField(blank=True)
    account = models.ForeignKey(MyProfile)
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.notes)
