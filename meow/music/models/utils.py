from django.db import models


class CreatedPublishedMixin(models.Model):

    class Meta:
        abstract = True

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )


class CardDataMixin(models.Model):
    
    class Meta:
        abstract = True

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="image/",
        null=True,
        blank=True
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=64
    )
