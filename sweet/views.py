from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostComment
from .forms import PostForm
from django.contrib import messages


def sweet(request):
    posts = Post.objects.order_by('-time').all()
    newPost = PostForm()

    if request.method == 'POST':
        newPost = PostForm(request.POST, request.FILES)
        if newPost.is_valid():
            postSaved = newPost.save(commit=True)
            postSaved.user = request.user
            postSaved.save()

        return redirect('sweet')
    else:
        return render(request, 'sweet/sweet.html', {'posts': posts,
                                                    'newPost': newPost})


def post(request, post_id):
    postSweet = get_object_or_404(Post, pk=post_id)

    comment = PostComment.objects.filter(post=postSweet)
    return render(request, 'sweet/post.html', {'postSweet': postSweet,
                                               'comment': comment})


def likePost(request):
    if request.method == "POST":
        post_id = request.POST.get('id')
        likePost = get_object_or_404(Post, pk=post_id)

        if likePost.likes.filter(id=request.user.id).exists():
            likePost.likes.remove(request.user)
        else:
            likePost.likes.add(request.user)

        likes = likePost.likes.count()

        if request.user in likePost.likes.all():
            likeStatus = "unlike"
        else:
            likeStatus = "like"

        return JsonResponse({'status': 1, "likes": likes, "likeStatus": likeStatus})
    else:
        return JsonResponse({'status': 0})


def postComment(request):
    if request.method == 'POST':
        postSerial = request.POST.get('postSerial')
        comment = request.POST.get('comment')
        user = request.user
        post = Post.objects.get(serial=postSerial)

        comment = PostComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Comment has been Posted Successfully ! ")

        return redirect(f'/{post.pk}')


def editPost(request, post_id):
    editPost = get_object_or_404(Post, pk=post_id)
    editPostForm = PostForm(instance=editPost)

    if request.method == 'POST':
        editPostForm = PostForm(request.POST, request.FILES, instance=editPost)
        if editPostForm.is_valid():
            editPostForm.save()
            return redirect(f'/{post_id}')
    else:
        return render(request, 'sweet/editPost.html', {'editPost': editPost, 'editPostForm': editPostForm})


def deletePost(request, post_id):
    deletePost = get_object_or_404(Post, pk=post_id)

    if request.user.is_authenticated:
        if request.user.id == deletePost.user.id:
            deletePost.delete()
            return redirect('sweet')
    else:
        return redirect('contact')


def deleteComment(request, comment_id):
    deleteComment = get_object_or_404(PostComment, pk=comment_id)

    if request.user.is_authenticated:
        if request.user.id == deleteComment.user.id:
            deleteComment.delete()
            return redirect(f'/{deleteComment.post.pk}')
    else:
        return redirect('sweet')
