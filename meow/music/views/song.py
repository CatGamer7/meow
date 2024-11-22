from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import (CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView)
from music.forms import SongForm
from music.models import Song


@method_decorator(staff_member_required, name='dispatch')
class SongCreateView(CreateView):
    template_name = "music/song/edit_form.html"
    form_class = SongForm
    
    def get_success_url(self):
        return reverse("music:song_detail", args=[self.object.pk])


@method_decorator(staff_member_required, name='dispatch')
class SongUpdateView(UpdateView):
    template_name = "music/song/edit_form.html"
    form_class = SongForm
    pk_url_kwarg = "song_id"
    model = Song

    def get_success_url(self):
        return reverse("music:song_detail", args=[self.object.pk])


@method_decorator(staff_member_required, name='dispatch')
class SongDeleteView(DeleteView):
    template_name = "music/song/edit_form.html"
    pk_url_kwarg = "song_id"
    model = Song

    def get_success_url(self):
        return reverse("pages:about")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SongForm(instance=self.object)
        return context
    

class SongDetailView(DetailView):
    template_name = "music/song/detail.html"
    pk_url_kwarg = "song_id"
    model = Song

    def get_object(self, queryset=None):
        return get_object_or_404(
            self.model.objects.select_related("album", "author"),
            pk=self.kwargs["song_id"]
        )
