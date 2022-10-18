import email
#from socket import fromshare heroku não usa este modulo então removi no deploy
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email =  forms.EmailField()

    #define o modelo com o qual será trabalhado ( similar a moongose)
    class Meta:
        model= User
        fields=['username', 'email', 'password1', 'password2']
