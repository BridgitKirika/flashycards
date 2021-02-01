from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import FlashCards


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



# class UserFlashForm(forms.ModelForm):
#     class Meta:
#         model = FlashCards
#         fields = ['flash_title', 'flash_description']
        