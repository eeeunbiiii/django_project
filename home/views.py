from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Velog
# Create your views here.

def home(request) :
    userlist = User.objects.all().order_by('id')
    velog_titles = Velog.objects.values_list('title', flat=True)  
    data = {
        'userlist': userlist,
        'velog_titles': velog_titles, 
    }
    return render(request, 'home/home.html', data)