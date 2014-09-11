"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client


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


    def test_fail(self):
        self.assertFalse(True)

    def test_view(self):
        client = Client()
        response = client.get('/')
        self.assertNotEqual(response.content, '')
