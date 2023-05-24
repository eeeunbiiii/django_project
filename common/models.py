from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #현 사용자 계정과  one to one 관계
    bio = models.CharField(max_length=64, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True)

# Create your models here.
