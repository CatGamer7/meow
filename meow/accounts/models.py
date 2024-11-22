from django.contrib.auth.models import User
from django.db import models
from music.models import Author, Song


class UserAccount(models.Model):
    
    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Profile",
        verbose_name="Пользователь авторизции"
    )

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
