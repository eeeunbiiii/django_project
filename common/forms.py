from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일") #이메일 속성 추가

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        #모듈 클래스 상속

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_image")