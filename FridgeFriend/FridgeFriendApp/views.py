from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import User, Item, Fridge, Category
import datetime


# Create your views here.
def index(request):
    template = loader.get_template('main.html')
    item_list = Item.objects.all()
    context = {
        "item_list":item_list
    }
    return HttpResponse(template.render(context))

def signin(request):
    return render(request, 'signin.html')

@csrf_exempt #let's revist this after the login page is made
def addrecord(request):
    name = request.POST['item']
    exp_date = request.POST['expdate']
    current_fridge = Fridge.objects.first()
    category_choice = Category.objects

    item = Item(item_name=name, expiry_date=exp_date,
                quantity=1, fridge_id=1, category_id=1)
    item.save()
    return HttpResponseRedirect(reverse('index'))

def deleterecord(request, id):
    item_  = Item.objects.get(id=id)
    item_.delete()
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def updaterecord(request, id):
    item_ = Item.objects.get(id=id)
    name = request.POST['item']
    exp_date = request.POST['expdate']

    item_.item_name = name
    item_.expiry_date = exp_date
    item_.save()
    return HttpResponseRedirect(reverse('index'))


    