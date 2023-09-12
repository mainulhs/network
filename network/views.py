from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Post, Comment


def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, "network/index.html", {
        "posts": posts,
        "comments": comments
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def new_post (request):
    if request.method == "POST":
        post = Post(
            user = request.user,
            post = request.POST["content"]
        )
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
    
def edit_post (request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.post = request.POST["content"]
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
    
def delete_post (request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
    
    
def like_post (request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.likes.add(request.user)
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
    
def comment (request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = Comment(
            user = User.objects.get(id=request.user.id),
            post = post,
            comment = request.POST["comment"]
        )
        comment.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
    
def edit_comment (request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        comment.comment = request.POST["comment"]
        comment.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
    
def delete_comment (request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")
