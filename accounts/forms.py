from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from difflib import SequenceMatcher

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30,min_length=5,required=True)
    email=forms.EmailField(max_length= 30, min_length=7, required=True)
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 



    
