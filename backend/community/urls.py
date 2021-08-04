from django.urls import path
from . import views

urlpatterns = [
    path('getlist/', views.getlist, name='getlist'),
    path('post_save/', views.post_save, name='post_save'),
]