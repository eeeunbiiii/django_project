from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Velog
# Create your views here.

def home(request) :
    userlist = User.objects.all().order_by('id')
    veloglist = Velog.objects.all()
    data = {
        'userlist': userlist,
        'veloglist': veloglist, 
    }
    return render(request, 'home/home.html', data)