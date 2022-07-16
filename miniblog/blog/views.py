from django.shortcuts import render, HttpResponseRedirect #12] because of this we can redirect the page  in to any page fr e.g logout
from .forms import SignUpForm, LoginForm, PostForm #16] here we are importing inbuilt django form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group 

# 9]  Home we are rendering home.html
def home(request):
 posts = Post.objects.all() #from podt model bring evry thing to post import also
 return render(request, 'blog/home.html', {'posts':posts})

# About
def about(request):
 return render(request, 'blog/about.html')

# Contact
def contact(request):
 return render(request, 'blog/contact.html')

# Dashboard if user is authenticated then go to dashboad or if not goo to login
def dashboard(request):
 if request.user.is_authenticated:
  posts = Post.objects.all()
  user = request.user
  full_name = user.get_full_name()
  gps = user.groups.all()
  return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps})
 else:
  return HttpResponseRedirect('/login/')

# Logout in logout we dont have render page we have to just run function
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/') #12] it redirects the page to home (go to model)

# 16] Sigup goto form.py file for cusmiztion of form
def user_signup(request):
 if request.method == "POST": #when we will fill the form and submit the request then post request will be there
  form = SignUpForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! You have become an Author.')#for writing messge we have to first import message
   user = form.save()
   group = Group.objects.get(name='Author') #if get request is there the blank fom will be seen 
   user.groups.add(group)
 else:
  form = SignUpForm()
 return render(request, 'blog/signup.html', {'form':form})

# Login
def user_login(request): #in login form we have to take data authenticate and send it too dashboard
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']#clean data means it converts the data in it proper type integer field dtata covert into integer character field dtata will be converted it into string type
    user = authenticate(username=uname, password=upass)#for using authinticate we have to import auth
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/dashboard/')
  else:
   form = LoginForm()
  return render(request, 'blog/login.html', {'form':form})
 else:
  return HttpResponseRedirect('/dashboard/')

# Add New Post
def add_post(request):
 if request.user.is_authenticated:
  if request.method == 'POST':
   form = PostForm(request.POST)
   if form.is_valid():
    title = form.cleaned_data['title']
    desc = form.cleaned_data['desc']
    pst = Post(title=title, desc=desc)
    pst.save()
    form = PostForm()
  else:
   form = PostForm()
  return render(request, 'blog/addpost.html', {'form':form})
 else:
  return HttpResponseRedirect('/login/')

# Update/Edit Post
def update_post(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Post.objects.get(pk=id)
      form = PostForm(request.POST, instance=pi)
      if form.is_valid():
        form.save()
    else:
      pi = Post.objects.get(pk=id)
      form = PostForm(instance=pi)
    return render(request, 'blog/updatepost.html', {'form':form})
  else:
    return HttpResponseRedirect('/login/')

# Delete Post
def delete_post(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Post.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/dashboard/')
  else:
    return HttpResponseRedirect('/login/')


#after making views gong to urls