from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.CharField(max_length=30)
    UserPW = models.CharField(max_length=30)

    def __str__(self):
        return self.UserID

class Post(models.Model) :
    title = models.CharField(max_length=50)
    writer_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    view_cnt = models.IntegerField(default=0)
    created_dt = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title