from django.db import models
from .album import Album
from .author import Author
from .utils import CreatedPublishedMixin, CardDataMixin


class Song(CreatedPublishedMixin, CardDataMixin):

    class Meta:
        abstract = False
        verbose_name = "Композиция"
        verbose_name_plural = "Композиции"
        ordering = ('-date_published',)

        error_template = "Количество {} должно быть неотрицательным"
        constraints = (
            models.CheckConstraint(
                check=models.Q(times_dowloaded__gte=0),
                name="CHECK gte download",
                violation_error_message=error_template.format("загрузок")
            ),
            models.CheckConstraint(
                check=models.Q(times_played__gte=0),
                name="CHECK gte played",
                violation_error_message=error_template.format("прослушиваний")
            )
        )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="songs",
        verbose_name="Автор"
    )
    
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="songs",
        verbose_name="Альбом"
    )

    date_published = models.DateTimeField(
        verbose_name="Дата публикации",
    )

    times_dowloaded = models.IntegerField(
        verbose_name="Количество загрузок",
        default=0,
    )

    times_played = models.IntegerField(
        verbose_name="Количество прослушиваний",
        default=0,
    )

    audio_file = models.FileField(
        verbose_name="Файл композиции",
        upload_to="audio/"
    )

    def __str__(self):
        return f"{self.album_type} - {self.name}"
