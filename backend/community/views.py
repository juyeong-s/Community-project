from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post
from .models import User

def getlist(requset):
    if requset.method == 'GET':
        user = list(User.objects.values())
        post = list(Post.objects.values())
        
        return JsonResponse(data=user, safe=False)