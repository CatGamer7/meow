from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('album/', views.AlbumListView.as_view(), name='album_list'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:album_id>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:album_id>/update/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:album_id>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),

    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:author_id>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:author_id>/like/', views.add_favorite_author_view, name='author_like'),
    path('author/<int:author_id>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:author_id>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),

    path('song/', views.SongListView.as_view(), name='song_list'),
    path('song/create/', views.SongCreateView.as_view(), name='song_create'),
    path('song/<int:song_id>/', views.SongDetailView.as_view(), name='song_detail'),
    path('song/<int:song_id>/download/', views.song_download_veiw, name='song_download'),
    path('song/<int:song_id>/play/', views.increase_song_played_view, name='song_play'),
    path('song/<int:song_id>/like/', views.add_favorite_song_view, name='song_like'),
    path('song/<int:song_id>/update/', views.SongUpdateView.as_view(), name='song_update'),
    path('song/<int:song_id>/delete/', views.SongDeleteView.as_view(), name='song_delete'),

    path('admin/', views.admin_panel_view, name='admin_panel')
]
