from django.forms import ModelForm
from music.models import Album


class AlbumForm(ModelForm):

    class Meta:
        exclude = ()
        model = Album
