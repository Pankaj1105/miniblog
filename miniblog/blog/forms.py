from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField  #this are builtin in django
from django.contrib.auth.models import User #this are builtin in django
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post

class SignUpForm(UserCreationForm): #making of signup form
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email',]
  labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'}), 
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
  #here we are settling clasess tahts we have make widgets ,with help of attrs we can put attributes, form control gives styling
  #go to login.html
  }

class LoginForm(AuthenticationForm):#we are using this form from django inbuilt api 
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'desc']
    labels = {'title':'Title', 'desc':'Description'}
    widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
    'desc':forms.Textarea(attrs={'class':'form-control'}), }

# 17 fo to adjustment of signup.html