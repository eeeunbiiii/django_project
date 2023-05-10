from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def login(request) :
    return render(request, 'user/login.html')

def logout(request) :
    return render(request, 'user/logout.html')

def register(request) :
    return render(request, 'user/register.html')
