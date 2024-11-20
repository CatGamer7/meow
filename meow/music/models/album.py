from django.db import models
from .utils import CreatedPublishedMixin, CardDataMixin


class Album(CreatedPublishedMixin, CardDataMixin):

    class Meta:
        abstract = False
        verbose_name = "Музыкальный альбом"
        verbose_name_plural = "Музыкальные альбомы"

    class AlbumType(models.TextChoices):
        BAND_ALBUM = ("BA", "Албом группы")
        COLLECTION = ("CL", "Коллекция")

    album_type = models.CharField(
        verbose_name="Тип альбома",
        max_length=2,
        choices=AlbumType.choices
    )

    def __str__(self):
        return f"{self.album_type} - {self.name}"
