from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm, ProfileForm
from common.models import Profile

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
    try :
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'common/mypage.html', {'profile':profile})
#Profile객체 가져오고 profile변수를 템플릿으로 전달

def setting(request):
    try:
        profile = request.user.profile  # 현재 로그인된 사용자의 프로필 가져오기
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)  # 프로필이 없을 경우 생성
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('common:mypage')
    else:
        form=ProfileForm(instance=profile)
    return render(request, 'common/mypage/setting.html', {'form': form})