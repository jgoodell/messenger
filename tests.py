"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class MessageTest(TestCase):
    def setUp(self):
        from datetime import datetime
        from messenger.models import Message
        self.text = "Testing 1... 2... 3..."
        self.message = Message(name="Tester",
                               text=self.text,
                               time_stamp=datetime.now())

    def test_message(self):
        self.assertEqual(unicode(self.text), unicode(self.message.text))
