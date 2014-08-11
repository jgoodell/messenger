"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class MessageTest(TestCase):
    """TestCase sub class for Message.
    """

    def setUp(self):
        """The test setup method. Run before each test.
        """
        from datetime import datetime
        from messenger.models import Message
        self.text = "Testing 1... 2... 3..."
        self.message = Message(name="Tester",
                               text=self.text,
                               time_stamp=datetime.now())

    def test_message(self):
        """Test that message returns unicode text when asked for the
        unicode representation of the type.
        """
        self.assertEqual(unicode(self.text), unicode(self.message))


    def test_fail(self):
        """A test designed to fail for helping in build pipeline
        configuration and development.
        """
        #self.assertFalse(True)
        pass
