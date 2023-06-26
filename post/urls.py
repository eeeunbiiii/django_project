from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('write/', views.post_write, name='post_write'),
    path('<int:pk>/', views.posting, name='posting'),
    path('<int:pk>/remove/', views.post_remove, name='post_remove'),
]