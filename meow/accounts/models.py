from django.contrib.auth.models import AbstractUser
from django.db import models
from music.models import Author, Song


class UserAccount(AbstractUser):

    class Meta:
        abstract = False
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    liked_songs = models.ManyToManyField(
        Song,
        verbose_name="Любимые композиции"
    )

    liked_authors = models.ManyToManyField(
        Author,
        verbose_name="Любимые авторы"
    )

    def __str__(self):
        return self.user.username
