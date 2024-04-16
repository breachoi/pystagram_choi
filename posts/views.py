from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.decorators.http import require_POST
from posts.forms import CommentForm
from django.shortcuts import render, redirect
from posts.models import Post, Comment


# Create your views here.
def feeds(request):

    if not request.user.is_authenticated:

        return redirect("/users/login/")

    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts": posts,
        "comment_form": comment_form,
    }
    return render(request, "posts/feeds.html", context)

@require_POST
def comment_add(request):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

        print(comment.id)
        print(comment.content)
        print(comment.user)

        return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")

@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
        return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
    else:
        return HttpResponseForbidden("You can't delete this comment")