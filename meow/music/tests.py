from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from music.models import Song, Author


class TestSong(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name="author",
            author_type=Author.AuthorType.BAND
        )

        return super().setUp()

    def test_song_creation(self):
        song = Song.objects.create(
            name="song_name",
            genre=Song.SongGenre.METAL,
            author=self.author,
            date_published=timezone.now(),
            audio_file=b""
        )

        self.assertTrue(song)

    def test_song_played_constraint(self):
        with self.assertRaises(IntegrityError):
            Song.objects.create(
                name="song_name",
                genre=Song.SongGenre.METAL,
                author=self.author,
                date_published=timezone.now(),
                audio_file=b"",
                times_played=-1
            )

    def test_song_download_constraint(self):
        with self.assertRaises(IntegrityError):
            Song.objects.create(
                name="song_name",
                genre=Song.SongGenre.METAL,
                author=self.author,
                date_published=timezone.now(),
                audio_file=b"",
                times_downloaded=-1
            )


class TestAdmin(TestCase):

    def test_rating(self):
        author = Author.objects.create(
            name="author",
            author_type=Author.AuthorType.BAND
        )

        for i in range(6):
            Song.objects.create(
                name=f"song_name_{i}",
                genre=Song.SongGenre.METAL,
                author=author,
                date_published=timezone.now(),
                audio_file=b"",
                times_played=i,
                times_downloaded=i
            )

        username = "test_user"
        password = "test_basedbasedbased"

        user_model = get_user_model()
        staff_user = user_model.objects.create(
            username=username,
            password=password,
            is_staff=True
        )

        client = Client()
        client.force_login(
            staff_user
        )

        response = client.get(reverse("music:admin_panel"))
        text = response.content.decode()

        self.assertNotIn("song_name_0", text)
