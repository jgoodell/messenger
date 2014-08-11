'''Contains class definitions for Messenger App.
'''

from django.db import models

class Message(models.Model):
    """Contains logic and attributes for managing a message
    instance.

    Attributes
    name:       CharField of max length 50
    text:       CharField of max length 200
    time_stamp: DateTimeField 'time stamp'
    """
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    time_stamp = models.DateTimeField('time stamp')

    def __unicode__(self):
        """Return the unicode representation of the type.
        """
        return self.text
