from django.db.models import deletion
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST
from .models import Post
from .models import User
from .forms import PostForm

def getPostlist(request):
    # users = User.objects.all()
    posts = Post.objects.all()
    # user_list = []
    # post_list = []
    if request.method == 'GET':
        # users = list(User.objects.values())
        posts = list(Post.objects.values())
    postdata = list(posts)

    return JsonResponse(postdata, safe=False)

def getUserlist(request):
    # users = User.objects.all()
    if request.method == 'GET':
        # users = list(User.objects.values())
        users = list(User.objects.values())

    userdata = list(users)

    return JsonResponse(userdata, safe=False)

@csrf_exempt
# @require_POST   # POST 메서드로 접근 시에만 동작
def postsave(request):
    if request.body:
        data = json.load(request.body)
        if 'posts' in data:
            posts = data['posts']
            Post.objects.all().delete()
            for post in posts:
                print('post',post)
                form = PostForm(post)
                if form.is_valid():
                    form.save() # DB에 저장
    return JsonResponse({})