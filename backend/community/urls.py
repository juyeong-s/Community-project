from django.urls import path
from . import views

urlpatterns = [
    path('getPostlist/', views.getPostlist, name='getPostlist'),
    path('postsave/', views.postsave, name='postsave'),
    path('getUserlist/', views.getUserlist, name='getUserlist'),
]