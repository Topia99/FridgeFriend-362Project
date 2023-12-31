from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Item, Fridge
from .forms import CreateUserForm, FridgeForm



# Create your views here.
@login_required(login_url='login')
def index(request, pk):
    template = loader.get_template('main.html')
    item_list = Item.objects.filter(fridge=pk).all()
    context = {
        "items": item_list,
        'fridge_id': pk,
        "request": request,
    }
    return HttpResponse(template.render(context))
    #TO-DO: look at register page and adjust render to avoid csrf error

#@login_required(login_url='login')
@csrf_exempt #let's revist this after the login page is made
def addrecord(request, pk):
    name = request.POST['item']
    exp_date = request.POST['expdate']

    item = Item(item_name=name, expiry_date=exp_date,
                quantity=1, fridge_id=pk)
    item.save()
    return redirect("fridge", pk)

@login_required(login_url='login')
def deleterecord(request, pk, id):
    item_  = Item.objects.get(id=id)
    item_.delete()
    return redirect("fridge", pk)

@login_required(login_url='login')
@csrf_exempt
def updaterecord(request, pk, id):
    item_ = Item.objects.get(id=id)
    name = request.POST['item_update']
    exp_date = request.POST['expdate_update']

    item_.item_name = name
    item_.expiry_date = exp_date
    item_.save()
    return redirect("fridge", pk)


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
@login_required(login_url='login')
def userProfile(request):
    fridge = Fridge.objects.prefetch_related('users').filter(users = request.user.id).all()
    template = loader.get_template('profile.html')
    context = {
        "fridges": fridge,
        "request": request,
    }
    return HttpResponse(template.render(context))



@login_required(login_url='login')
def createFridge(request):
    form = FridgeForm()

    if request.method == 'POST':
        form = FridgeForm(request.POST)
        if form.is_valid():
            fridge_instance = form.save(commit=False)  # Save the form temporarily without committing to the database
            fridge_instance.save()  # Now save the instance to the database
            fridge_instance.users.set([request.user])  # Set the many-to-many relationship
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'create_fridge.html', context)
            