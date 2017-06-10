from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)


class Post(models.Model):
    title = models.CharField(
        max_length=60,
        null=False,
        blank=False)
    body = models.TextField(
        null=True,
        blank=False)
    image = models.ImageField(
        upload_to='post_images/',
        default='post_images/test_picture.jpg',
        null=True,
        blank=True)
    likers = models.ManyToManyField(
        CustomUser,
        related_name='likers',
        blank=True)
    author = models.ForeignKey(
        CustomUser,
        related_name='author',
        null=False,
        blank=False)

    def __str__(self):
        return '{}'.format(self.title)


class PostComment(models.Model):
    body = models.TextField(
        null=True,
        blank=False)
    author = models.ForeignKey(
        CustomUser,
        related_name='comment_author',
        null=False,
        blank=False),
    publication_date = models.DateField(
        default=datetime.now,
        blank=False)
    post = models.ForeignKey(
        Post,
        related_name='related_post',
        null=False,
        blank=False)

    def __str__(self):
        return '{}, {}'.format(self.author, self.publication_date)
