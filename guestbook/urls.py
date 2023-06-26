from django.urls import path
from django.contrib import admin
from . import views

app_name = 'guestbook'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('delete/', views.delete, name='delete'),
    path('deleteform/<int:id>/', views.deleteform, name='deleteform'),
]