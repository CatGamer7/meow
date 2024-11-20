from django.db import models


class CreatedPublishedMixin(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        abstract = True
