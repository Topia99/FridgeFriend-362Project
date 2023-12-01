from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Fridge


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class FridgeForm(ModelForm):
    class Meta:
        model = Fridge
        fields = ['fridge_name']
        exclude = ['users']
        
    # fridge_name = forms.CharField(max_length=255)
    # users = forms.IntegerField(required=False)
