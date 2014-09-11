from django.http import HttpResponse

from messenger.models import Message

def root(request):
    
    messages = Message.objects.all()
    return HttpResponse("Hello world! There are %s messages." % len(messages))
