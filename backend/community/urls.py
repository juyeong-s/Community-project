from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.postlist, name='postlist'),
    
]