from django.db import models
from .album import Album
from .author import Author
from .utils import CreatedPublishedMixin, CardDataMixin


class Song(CreatedPublishedMixin, CardDataMixin):

    class Meta:
        abstract = False
        verbose_name = "Композиция"
        verbose_name_plural = "Композиции"
        ordering = ("-date_published",)

        constraints = (
            models.CheckConstraint(
                check=models.Q(times_downloaded__gte=0),
                name="CHECK gte download"
            ),
            models.CheckConstraint(
                check=models.Q(times_played__gte=0),
                name="CHECK gte played"
            )
        )
        
    class SongGenre(models.TextChoices):
        POP = ("Поп", "Поп")
        ROCK = ("Рок", "Рок")
        METAL = ("Метал", "Метал")

    genre = models.CharField(
        verbose_name="Жанр",
        max_length=32,
        choices=SongGenre.choices
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

    times_downloaded = models.IntegerField(
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
        return f"{self.author.name} - {self.name}"
