from django.urls import path
from . import views

urlpatterns = [
    path('getPostlist/', views.getPostlist, name='getPostlist'),
    path('post_save/', views.post_save, name='post_save'),
    path('getUserlist/', views.getUserlist, name='getUserlist'),
]