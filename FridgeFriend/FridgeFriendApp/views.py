from django.http import HttpResponse
from django.template import loader
from .models import User, Item

# Create your views here.
def index(request):
    template = loader.get_template('main.html')
    item_list = Item.objects.all()
    context = {
        "item_list":item_list
    }
    return HttpResponse(template.render(context))