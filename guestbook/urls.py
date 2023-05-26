from django.urls import path
from django.contrib import admin
import guestbook.views as guestbook_views

app_name = 'guestbook'
urlpatterns = [
    path('/list', guestbook_views.list, name='list'),
    path('/write', guestbook_views.write, name='write'),
    path('/deleteform/<int:id>', guestbook_views.deleteform, name='deleteform'),
    path('/delete', guestbook_views.delete, name='delete'),
]