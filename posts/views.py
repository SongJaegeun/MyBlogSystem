from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def p_list(request):
    if 'user' in request.session.keys():
        my_list = Post.objects.all().order_by('-id')

        session = request.session['user']
        context = {'posts': my_list,
                   'session': session}

        return render(request, 'list.html', context)
    else:

        return render(request, 'error.html')


@login_required
def p_create(request):
    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(username=user_id)
            new_post = Post(
                author=user,
                title=post_form.cleaned_data['title'],
                contents=post_form.cleaned_data['contents']
            )
            new_post.save()
            return redirect('posts:list')

    else:
        # GET 방식으로 호출 될 때
        post_form = PostForm()

    return render(request, 'create.html', {'post_form': post_form})

@login_required
def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)
    post.delete()

    return redirect('posts:list')


@login_required
def p_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        # GET 방식으로 호출 될 때
        post_form = PostForm(instance=post)

    return render(request, 'update.html', {'post_form': post_form})


@login_required
def p_update2(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        post_form = PostForm(request.POST, instance=post)
        print(post_form)

        if post_form.is_valid():
            post_form.save()
            return redirect(f'/posts/{post_id}/read/')

    else:
        # GET 방식으로 호출 될 때
        post_form = PostForm(instance=post)

    return render(request, 'update.html', {'post_form': post_form})


@login_required
def p_read(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    session = request.session['user']
    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        user_id = request.session.get('user')
        user = User.objects.get(username=user_id)
        comment = Comment(post=post, author=user_id)
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():

            comment_form.save()
            return redirect(f'/posts/{post_id}/read')

    else:
        # GET 방식으로 호출 될 때
        comment_form = CommentForm()

        context = {'post': post,
                   'comment_form': comment_form,
                   'session': session}
    return render(request, 'read.html', context)


@login_required
def c_delete(request, post_id, comment_id):
    print(comment_id)
    comment = Comment.objects.get(id=comment_id)
    print(comment)
    comment.delete()

    return redirect(f'/posts/{post_id}/read/')


