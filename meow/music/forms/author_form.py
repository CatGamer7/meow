from django.forms import ModelForm
from music.models import Author


class AuthorForm(ModelForm):

    class Meta:
        exlude = ()
        model = Author
