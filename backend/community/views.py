from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST
from .models import Post
from .models import User
from django.shortcuts import redirect
from django.db.models import Q
from django.core import serializers

def usersearch(postdata, userdata):
    username = []
    for post in postdata:
        for user in userdata:
            if post["writer_fk_id"] == user["id"]:
                username.append(user["UserID"])
    return username


def getPostlist(request):
    if request.method == 'GET':
        # users = list(User.objects.values())
        postdata = list(Post.objects.values())
        postdata.reverse()
        # userdata = list(User.objects.values('id','UserID'))
        # username = usersearch(postdata,userdata)
    # postdata = list(posts)

    return JsonResponse(postdata, safe=False)

def getUserlist(request):
    # users = User.objects.all()
    if request.method == 'GET':
        postdata = list(Post.objects.values())
        userdata = list(User.objects.values('id','UserID'))

    username = usersearch(postdata,userdata)
    return JsonResponse(username, safe=False)

@csrf_exempt
@require_POST   # POST 메서드로 접근 시에만 동작
def postsave(request):
    print(123)
    
    if request.body:
        data = request.body.decode('utf-8')
        post = json.loads(data)
        id = post['id']
        # 수정 시
        if Post.objects.filter(id=id).exists():
            posts = Post.objects.get(id=id)
            posts.title = post['title']
            posts.content = post['content']
            posts.writer_fk_id = post['writer_fk_id']
            posts.save()
            return HttpResponse('Edit success')
        # post 올릴 시
        title = post['title']
        writer_fk_id = post['writer_fk_id']
        content = post['content']
        user = User.objects.get(id=writer_fk_id)

        posts = Post(title=title, writer_fk=user, content=content)
        posts.save()

    return HttpResponse('Save success')

@csrf_exempt
@require_POST
def viewcnt_save(request):
    print(123)
    if request.body:
        data = request.body.decode('utf-8')
        get_data = json.loads(data)

        post = Post.objects.get(id=get_data["id"])
        print(post.view_cnt)
        post.view_cnt = get_data["view_cnt"]
        post.save()

        return HttpResponse('success')

def pagedpostlist(request, id):
    postlist = list(Post.objects.values())
    paginator = Paginator(postlist, 10)
    print(paginator)
    page = request.GET.get('page')
    print(page)
    try:
        post = paginator.page(page)
        print(1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(id)
        print(2)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)
        print(3)
    return HttpResponse(post)

@csrf_exempt
def postdelete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponse({})

def uploadImg(request, id):
    data = request.body.decode('utf-8')
    print(data)
    return HttpResponse(data)

def searchKeyword(request, keyword):
    if keyword:
        posts = Post.objects.filter(title__icontains=keyword)
        postlist = list(posts.values())
    else:
        postlist = list(Post.objects.values())
        postlist.reverse()

    return JsonResponse(postlist, safe=False)
