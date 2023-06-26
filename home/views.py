from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def home(request) :
    userlist = User.objects.all().order_by('id')
    data = {'userlist' : userlist}
    return render(request, 'home/home.html', data)