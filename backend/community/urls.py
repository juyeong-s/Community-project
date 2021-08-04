from django.urls import path
from . import views

urlpatterns = [
    path('getlist/', views.getlist, name='getlist'),

]