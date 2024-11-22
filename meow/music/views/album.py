from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import (CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView)
from music.forms import AlbumForm
from music.models import Album


@method_decorator(staff_member_required, name='dispatch')
class AlbumCreateView(CreateView):
    template_name = "music/album/edit_form.html"
    form_class = AlbumForm
    
    def get_success_url(self):
        return reverse("music:album", args=[self.object.pk])


@method_decorator(staff_member_required, name='dispatch')
class AlbumUpdateView(UpdateView):
    template_name = "music/album/edit_form.html"
    form_class = AlbumForm
    pk_url_kwarg = "album_id"
    model = Album

    def get_success_url(self):
        return reverse("music:album", args=[self.object.pk])


@method_decorator(staff_member_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    template_name = "music/album/edit_form.html"
    pk_url_kwarg = "album_id"
    model = Album

    def get_success_url(self):
        return reverse("pages:about")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AlbumForm(instance=self.object)
        return context
    

class AlbumDetailView(DetailView):
    template_name = "music/album/detail.html"
    pk_url_kwarg = "album_id"
    model = Album
