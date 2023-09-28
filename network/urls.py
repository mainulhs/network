
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
    path("like_post/<int:post_id>", views.like_post, name="like_post"),
    path("comment/<int:post_id>", views.comment, name="comment"),
    path("edit_comment/<int:comment_id>", views.edit_comment, name="edit_comment"),
    path("delete_comment/<int:comment_id>", views.delete_comment, name="delete_comment"),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow/', views.follow, name='follow'),
    path('<str:username>/unfollow/', views.unfollow, name='unfollow'),
    path('following/<str:username>/', views.following, name='following'),
]
