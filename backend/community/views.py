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
@require_POST   # POST 메서드로 접근 시에만 동작
def postsave(request, *args, **kwargs):
    print(123)
    if request.body:
        print(request.body.decode('utf-8'))
        data = request.body.decode('utf-8')
        print(type(data))
        print(data.title)
        post = json.loads(data)
        print(post)
        # data = json.load(body_unicod)
        # if 'title' in data:
        #     posts = data["title"]
            # Post.objects.all().delete()
            # for post in posts:
            #     print('post',post)
        form = PostForm(post)
        print(form)
        if form.is_valid():
            print('saved')
            form.save() # DB에 저장

    return HttpResponse('success')