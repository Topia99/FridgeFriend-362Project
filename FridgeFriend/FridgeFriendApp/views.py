from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Item, Fridge, Category
from .forms import CreateUserForm, FridgeForm



# Create your views here.
@login_required(login_url='login')
def index(request, pk):
    template = loader.get_template('main.html')
    item_list = Item.objects.filter(fridge=pk).all()
    context = {
        "items": item_list,
        "request": request,
    }
    return HttpResponse(template.render(context))

#@login_required(login_url='login')
@csrf_exempt #let's revist this after the login page is made
def addrecord(request, pk):
    name = request.POST['item']
    exp_date = request.POST['expdate']
    current_fridge = Fridge.objects.first()
    category_choice = Category.objects

    item = Item(item_name=name, expiry_date=exp_date,
                quantity=1, fridge_id=pk, category_id=1)
    item.save()
    return redirect('user')

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
        return redirect('user')
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
                return redirect('user')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# Display user's fridge
def userProfile(request):
    fridge = Fridge.objects.prefetch_related('users').filter(users = request.user.id).all()
    template = loader.get_template('profile.html')
    context = {
        "fridges": fridge,
        "request": request,
    }
    return HttpResponse(template.render(context))


def createFridge(request):
    form = FridgeForm()
    
    if request.method == 'POST':
        form = FridgeForm(request.POST)
        form.users = request.user.id
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'create_fridge.html', context)
            