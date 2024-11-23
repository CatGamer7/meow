from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            if self.object in user.liked_songs.all():
                context["liked"] = True

        return context


class SongListView(ListView):
    template_name = "music/song/list.html"
    paginate_by = settings.PER_PAGE
    model = Song

    def get_queryset(self):
        now = timezone.now()

        return self.model.objects.select_related(
            "album", "author"
        ).filter(
            date_published__lte=now,
            is_published=True,
            author__is_published=True,
        ).order_by("-date_published")


@require_POST
def song_download_veiw(request, song_id):
    song_obj = _get_published_song_by_id(song_id)

    if not song_obj:
        raise Http404(f"Композиция с ключом {song_id} не существует")

    song_obj.times_downloaded += 1
    song_obj.save()

    return FileResponse(
        song_obj.audio_file.file,
        as_attachment=True,
        filename=f"{song_obj}.mp3"
    )


@require_POST
def increase_song_played_view(request, song_id):
    song_obj = _get_published_song_by_id(song_id)

    if not song_obj:
        raise Http404(f"Композиция с ключом {song_id} не существует")

    song_obj.times_played += 1
    song_obj.save()

    return HttpResponse()


@require_POST
@login_required
def add_favorite_song_view(request, song_id):
    song_obj = _get_published_song_by_id(song_id)

    if not song_obj:
        raise Http404(f"Композиция с ключом {song_id} не существует")

    if request.POST["like"] == 'true':
        request.user.liked_songs.add(song_obj)
    else:
        request.user.liked_songs.remove(song_obj)

    request.user.save()
    return HttpResponse()


def _get_published_song_by_id(song_id: int) -> Song:
    now = timezone.now()
    song = get_object_or_404(
        Song.objects.prefetch_related("author", "album"),
        date_published__lte=now,
        is_published=True,
        author__is_published=True,
        pk=song_id
    )

    return song
