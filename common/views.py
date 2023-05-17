from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def mypage(request):
    return render(request, 'common/mypage.html')

def setting(request):
    return render(request, 'common/mypage/setting.html')