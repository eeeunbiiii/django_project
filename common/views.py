from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from common.forms import UserForm, ProfileForm
from common.models import Profile
from django.contrib.auth.models import User

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

def mypage(request, id):
    selected_user = get_object_or_404(User, id=id)
    try :
        profile = Profile.objects.get(user=selected_user)
    except Profile.DoesNotExist:
        profile = None
    context = {'selected_user': selected_user, 'profile': profile}
    return render(request, 'common/mypage.html', context)
#Profile객체 가져오고 profile변수를 템플릿으로 전달

def setting(request, id):
    try:
        profile = request.user.profile  # 현재 로그인된 사용자의 프로필 가져오기
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)  # 프로필이 없을 경우 생성
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('common:mypage', id=id)
    else:
        form=ProfileForm(instance=profile)
    return render(request, 'common/mypage/setting.html', {'form': form})