from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from django.contrib.sessions.models import Session
from .forms import *
from .models import Ngo
from .models import Donation


def home(request):
   return render(request,template_name='index.html')
def contact(request):
   return render(request,template_name='contact.html')
def about(request):
   return render(request,template_name='aboutus.html')
def profile(request):
   return render(request,template_name='profile.html')
def thankyou(request):
   return render(request,template_name='thankyou.html')
def ngo(request):
   return render(request,template_name='ngo.html')   


def dlist(request):
    dlist=Donation.objects.all()
    context= {
        'dlist': dlist,
    }

    return render(request,template_name='dlist.html', context=context )

def donation(request):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    context ={
        'form':form,
    }
    return render(request,template_name='donation.html', context=context)
   

def user_sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username , email=email , password = password)

        request.session['signup_username']= username
        request.session['signup_email'] = email
        request.session['signup_password'] = password

        user = authenticate(request,username=username , password = password)

        if user is not None :
            auth_login(request,user)
            messages.success(request,'Successfulyy signed up!')
            return redirect('user_login')
    return render(request,template_name='User_Signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            auth_login(request,user)
            messages.success(request,'Successfulyy Logged In!')
            return redirect('user_home')
    return render(request,template_name='User_Login.html')

def logout_user(request):
     logout(request)
     messages.success(request,'Youre logged out!')
     return redirect('user_login')