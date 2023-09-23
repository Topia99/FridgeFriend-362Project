from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def food_entry(request):
    if request.method == 'POST':
        food_name = request.POST.get("food_name")
        quantity = request.POST.get("quantity")
        
        

