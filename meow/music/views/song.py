from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.utils import timezone
from django.views.generic import (CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView,
                                  ListView)
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


class SongListView(ListView):
    template_name = "music/song/list.html"
    paginate_by = settings.PER_PAGE
    model = Song

    def get_queryset(self):
        now = timezone.now()

        return self.model.objects.select_related(
            "album", "author"
        ).filter(
            pub_date__lte=now,
            is_published=True,
            author_is_published=True,
            albumn_is_published=True,
        ).order_by("-date_published")


def song_download_veiw(request, song_id):
    song_obj = _get_published_song_by_id(song_id)

    if not song_obj:
        raise Http404("Композиция не существует")
    
    song_obj.times_dowloaded += 1
    song_obj.save()

    file_to_send = ContentFile(song_obj.audio_file, f"{song_obj}.mp3")
    response = HttpResponse(file_to_send)
    response["Content-Type"] = "audio/mpeg"
    response["Content-Length"] = file_to_send.size

    return response


def increase_song_played_view(request, song_id):
    song_obj = _get_published_song_by_id(song_id)

    if not song_obj:
        raise Http404("Композиция не существует")

    song_obj.times_played += 1
    song_obj.save()

    return HttpResponse()


def add_favorite_song_view(request, song_id):
    song_obj = _get_published_song_by_id(song_id)

    if not song_obj:
        raise Http404("Композиция не существует")

    profile = request.user.profile
    profile.liked_songs.add(song_obj)

    return HttpResponse()


def _get_published_song_by_id(song_id: int) -> Song:
    now = timezone.now()
    song = get_object_or_404(
        Song.objects.prefetch_related("author", "album"),
        pub_date__lte=now,
        is_published=True,
        author_is_published=True,
        albumn_is_published=True,
        pk=song_id
    )

    return song
