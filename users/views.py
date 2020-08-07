from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.forms import UserForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def log_in(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            request.session['user'] = user.username
            return redirect('/')
        else:
            return HttpResponse('아이디와 패스워드를 다시 확인해주세요')

    else:
        login_form = LoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def join(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create_user(**user_form.cleaned_data)
            return redirect('/')

    else:
        user_form = UserForm()

    return render(request, 'join.html', {'user_form': user_form})


@login_required
def log_out(request):
    logout(request)
    return redirect('/')

@login_required
def mypage(request):
    session = request.session['user']
    print(session)
    user = get_object_or_404(User, username=session)

    return render(request, 'mypage.html', {'user': user})