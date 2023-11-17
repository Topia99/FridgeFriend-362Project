from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Item, Fridge, Category
from .forms import CreateUserForm


# Create your views here.
@login_required(login_url='login')
def index(request):
    template = loader.get_template('main.html')
    item_list = Item.objects.all()
    context = {
        "items": item_list,
        "request": request,
    }
    return HttpResponse(template.render(context))

#@login_required(login_url='login')
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

@login_required(login_url='login')
def deleterecord(request, id):
    item_  = Item.objects.get(id=id)
    item_.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login')
@csrf_exempt
def updaterecord(request, id):
    item_ = Item.objects.get(id=id)
    name = request.POST['item']
    exp_date = request.POST['expdate']

    item_.item_name = name
    item_.expiry_date = exp_date
    item_.save()
    return HttpResponseRedirect(reverse('index'))

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    
    context = {'form': form}
    return render(request, 'register.html', context)
    
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            
            # Get user input from login.html
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # autheticate user
            user = authenticate(request, username=username, password=password)
            
            # Check whether user exist
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def userProfile(request):
    return render(request, 'profile.html')