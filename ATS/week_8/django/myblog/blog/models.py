from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class HidePostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=True)


class ShowPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='pictures/')


    def __str__(self):
        return f'{self.firstname} - {self.lastname}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    is_hidden = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    objects = models.Manager()
    deleted_object = HidePostManager()
    active_object = ShowPostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    objects = models.Manager()
    deleted_object = HidePostManager()
    active_object = ShowPostManager()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.pk)))


class Profile(models.Model):
    name = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



