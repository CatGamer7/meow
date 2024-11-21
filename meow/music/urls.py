from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('album/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/update/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    
    path('song/create/', views.SongCreateView.as_view(), name='song_create'),
    path('song/update/', views.SongUpdateView.as_view(), name='song_update'),
    path('song/delete/', views.SongDeleteView.as_view(), name='song_delete'),
]
