from django.contrib import admin
from community.models import Post
from community.models import User

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(User)
