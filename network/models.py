from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} posted {self.post} on {self.timestamp}"
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented {self.comment} on {self.post} on {self.timestamp}"

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follows")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} followed {self.follower} on {self.timestamp}"

    
