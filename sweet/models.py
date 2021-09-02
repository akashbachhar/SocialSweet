from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    serial = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    time = models.DateTimeField(default=now)
    likes = models.ManyToManyField(User, related_name='post_like')

    def __str__(self):
        return f"{self.content[0:50]} by {self.user.first_name}"


class PostComment(models.Model):
    serial = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + '...' + ' by ' + self.user.first_name
