from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
#     user_id = models.CharField('아이디', max_length=20, unique=True)
#     user_nm = models.CharField('이름', max_length=10)
#     user_pw = models.CharField('비밀번호', max_length=20)
#     email = models.EmailField('이메일', max_length=50)
#     reg_time = models.DateTimeField('가입일', auto_now_add=True)
#
#     def __str__(self):
#         return self.user_id
