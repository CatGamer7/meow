from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import (CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView,
                                  ListView)
from music.forms import AuthorForm
from music.models import Author


@method_decorator(staff_member_required, name='dispatch')
class AuthorCreateView(CreateView):
    template_name = "music/author/edit_form.html"
    form_class = AuthorForm
    
    def get_success_url(self):
        return reverse("music:author_detail", args=[self.object.pk])


@method_decorator(staff_member_required, name='dispatch')
class AuthorUpdateView(UpdateView):
    template_name = "music/author/edit_form.html"
    form_class = AuthorForm
    pk_url_kwarg = "author_id"
    model = Author

    def get_success_url(self):
        return reverse("music:author_detail", args=[self.object.pk])


@method_decorator(staff_member_required, name='dispatch')
class AuthorDeleteView(DeleteView):
    template_name = "music/author/edit_form.html"
    pk_url_kwarg = "author_id"
    model = Author

    def get_success_url(self):
        return reverse("pages:about")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthorForm(instance=self.object)
        return context

class AuthorDetailView(DetailView):
    template_name = "music/author/detail.html"
    pk_url_kwarg = "author_id"
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page_obj = Paginator(
            self.object.songs.all(),
            settings.PER_PAGE
        )
        page_obj = page_obj.get_page(self.request.GET.get("page"))

        context["page_obj"] = page_obj
        return context


class AuthorListView(ListView):
    template_name = "music/author/list.html"
    paginate_by = settings.PER_PAGE
    model = Author

    def get_queryset(self):
        return self.model.objects.filter(
            is_published=True
        ).order_by("-created_at")


def add_favorite_author_view(request, author_id):
    song_obj = _get_published_author_by_id(author_id)

    if not song_obj:
        raise Http404("Композиция не существует")

    profile = request.user.profile
    profile.liked_authors.add(song_obj)

    return HttpResponse()


def _get_published_author_by_id(author_id: int) -> Author:
    author = get_object_or_404(
        Author.objects.prefetch_related("author", "album"),
        is_published=True,
        pk=author_id
    )

    return author
