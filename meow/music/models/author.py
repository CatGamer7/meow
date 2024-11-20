from django.db import models
from .utils import CreatedPublishedMixin


class Author(CreatedPublishedMixin):

    class Meta:
        abstract = False
        verbose_name = "Музыкальный автор"
        verbose_name_plural = "Музыкальные авторы"

    class AuthorType(models.TextChoices):
        BAND = ("BD", "Группа")
        SOLO = ("SL", "Сольный исполнитель")
        ORCHESTRA = ("OR", "Оркестр")
        ENSEMBLE = ("EN", "Ансамбль")

    author_type = models.CharField(
        verbose_name="Тип автора",
        max_length=2,
        choices=AuthorType.choices
    )

    stage_name = models.CharField(
        verbose_name="Имя автора",
        max_length=64
    )

    def __str__(self):
        return f"{self.author_type} - {self.stage_name}"
