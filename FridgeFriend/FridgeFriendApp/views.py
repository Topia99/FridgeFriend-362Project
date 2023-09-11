from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    current_time = datetime.datetime.now();
    html = "<html><body><h1>Fridge Friend</h1><p>Current time: %s</p></body></html>" % current_time
    return HttpResponse(html)