from django.db import models
from .utils import CreatedPublishedMixin, CardDataMixin


class Author(CreatedPublishedMixin, CardDataMixin):

    class Meta:
        abstract = False
        verbose_name = "Музыкальный автор"
        verbose_name_plural = "Музыкальные авторы"
        ordering = ('-created_at',)

    class AuthorType(models.TextChoices):
        BAND = ("Группа", "Группа")
        SOLO = ("Сольный исполнитель", "Сольный исполнитель")
        ORCHESTRA = ("Оркестр", "Оркестр")
        ENSEMBLE = ("Ансамбль", "Ансамбль")

    author_type = models.CharField(
        verbose_name="Тип автора",
        max_length=32,
        choices=AuthorType.choices
    )

    def __str__(self):
        return self.name
