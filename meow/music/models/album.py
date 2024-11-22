from django.db import models
from .utils import CreatedPublishedMixin, CardDataMixin


class Album(CreatedPublishedMixin, CardDataMixin):

    class Meta:
        abstract = False
        verbose_name = "Музыкальный альбом"
        verbose_name_plural = "Музыкальные альбомы"
        ordering = ('-created_at',)

    class AlbumType(models.TextChoices):
        BAND_ALBUM = ("Албом группы", "Албом группы")
        COLLECTION = ("Коллекция", "Коллекция")

    album_type = models.CharField(
        verbose_name="Тип альбома",
        max_length=32,
        choices=AlbumType.choices
    )

    def __str__(self):
        return self.name
