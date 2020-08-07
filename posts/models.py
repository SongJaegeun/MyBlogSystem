from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE)

    title = models.CharField('글제목', max_length=50)
    contents = models.TextField('글내용', max_length=1000)

    def __str__(self):
        return self.contents


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField('댓글 작성자', max_length=20)
    comments = models.TextField('댓글', max_length=100)

    def __str__(self):
        return self.comments

