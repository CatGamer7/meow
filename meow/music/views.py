from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import User
from django.db.models.manager import BaseManager
from django.views.generic.edit import (CreateView,
                                       DeleteView,
                                       UpdateView)
from .forms import (AlbumForm,
                    AuthorForm,
                    SongForm)
from datetime import datetime, timezone


PER_PAGE = 10


class AlbumCreateView(CreateView, PermissionRequiredMixin):
    template_name = ""
    form_class = AlbumForm


class AlbumUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = ""
    form_class = AlbumForm
    pk_url_kwarg = 'author_id'


class AlbumDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = ""
    pk_url_kwarg = 'author_id'


class AuthorCreateView(CreateView, PermissionRequiredMixin):
    template_name = ""
    form_class = AuthorForm


class AuthorUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = ""
    form_class = AuthorForm
    pk_url_kwarg = 'author_id'


class AuthorDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = ""
    pk_url_kwarg = 'author_id'


class SongCreateView(CreateView, PermissionRequiredMixin):
    template_name = ""
    form_class = SongForm


class SongUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = ""
    form_class = SongForm
    pk_url_kwarg = 'author_id'


class SongDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = ""
    pk_url_kwarg = 'author_id'
