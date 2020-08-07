

from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', views.log_out, name='logout'),
    path('mypage/', views.mypage, name='mypage')

]
