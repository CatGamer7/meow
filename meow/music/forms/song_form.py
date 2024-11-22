from django.forms import ModelForm, DateInput
from music.models import Song


class SongForm(ModelForm):

    class Meta:
        exclude = ('times_dowloaded', 'times_played')
        widgets = {
            'date_published': DateInput(attrs={'type': 'date'})
        }
        model = Song
