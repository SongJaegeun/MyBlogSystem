
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView

# http://localhost:8000 호출 시 전체 프로젝트의 홈페이지로 이동
# Django_는 elegant URL 지원
# 정규표현식(regular expression)
# 시작 => ^
# 끝  => $
# [0-9] : 1글자 지칭
# {3} : 3번 반복
# {3,5} : 3번 ~ 5번 반복(3,4,5)
# [0-9]{4} : 0~9 숫자가 4번 반복 = 4자리 숫자
# r(raw) : escape 문자를 한번 더 사용하지 않도록 처리
# \d : 0~9를 지칭
# ex) r"^[0-9]{1,3}$"
# r"^010[1-9]\d{6,7}$"

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name='index.html'), name="home"),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls'))
]
