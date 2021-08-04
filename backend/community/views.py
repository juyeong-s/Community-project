from django.db.models import deletion
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_POST
from .models import Post
from .models import User
from .forms import PostForm

def getlist(requset):
    users = User.objects.all()
    posts = Post.objects.all()
    # user_list = []
    # post_list = []
    if requset.method == 'GET':
        # users = list(User.objects.values())
        posts = list(Post.objects.values())
    data = list(posts)
    # data.append(posts)
    # for index, user in enumerate(users, start=1):
    #     user_list.append({'id':index, 'UserID':user.UserID, 'UserPW':user.UserPW})
        
    # for index, post in enumerate(posts, start=1):
    #     post_list.append({'id':index, 'title':post.title, 'writer_fk':post.writer_fk, 'content':post.content, 'created_dt':post.created_dt, 'modified':post.modified}.decode('utf8'))
    # post_list = list(post_list.values())
    # data = {user_list,post_list}
    # print(data)
    # data.append(user_list)
    return JsonResponse(data, safe=False)

@require_POST   # POST 메서드로 접근 시에만 동작
def post_save(request):
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