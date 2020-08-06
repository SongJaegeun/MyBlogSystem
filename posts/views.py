from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm
# Create your views here.


def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    context = {'posts': my_list}

    return render(request, 'list.html', context)


def p_create(request):
    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        # GET 방식으로 호출 될 때
        post_form = PostForm()

    return render(request, 'create.html', {'post_form': post_form})


def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)
    post.delete()

    return redirect('posts:list')


def p_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        post_form = PostForm(request.POST, instance=post)
        print(post_form)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        # GET 방식으로 호출 될 때
        post_form = PostForm(instance=post)

    return render(request, 'update.html', {'post_form': post_form})


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


def p_read(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        # POST 방식으로 호출 될 때
        comment = Comment(post=post)
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():

            comment_form.save()
            return redirect(f'/posts/{post_id}/read')

    else:
        # GET 방식으로 호출 될 때
        comment_form = CommentForm()

        context = {'post': post,
                   'comment_form': comment_form}
    return render(request, 'read.html', context)


def c_delete(request, post_id, comment_id):
    print(comment_id)
    comment = Comment.objects.get(id=comment_id)
    print(comment)
    comment.delete()

    return redirect(f'/posts/{post_id}/read/')


