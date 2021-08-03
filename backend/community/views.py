from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post
from .models import User

def postlist(requset):
    if requset.method == 'GET':
        post = list(Post.objects.values())
        return JsonResponse(post, safe=False)