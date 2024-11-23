from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from music.models import Song


@staff_member_required
def admin_panel_view(request):
    download_rating = Song.objects.values("pk", "name", "times_downloaded").order_by("-times_downloaded")[:5]
    played_rating = Song.objects.values("pk", "name", "times_played").order_by("-times_played")[:5]

    context = {
        "download_rating": download_rating,
        "played_rating": played_rating
    }

    return render(request, "music/admin.html", context)
