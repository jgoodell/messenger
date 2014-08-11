from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    time_stamp = models.DateTimeField('time stamp')

    def __unicode__(self):
        return self.text
