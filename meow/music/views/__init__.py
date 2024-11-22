from .admin import admin_panel_view
from .album import (AlbumCreateView,
                    AlbumUpdateView,
                    AlbumDeleteView,
                    AlbumDetailView,
                    AlbumListView)
from .author import (AuthorCreateView,
                     AuthorUpdateView,
                     AuthorDeleteView,
                     AuthorDetailView,
                     AuthorListView,
                     add_favorite_author_view)
from .song import (SongCreateView,
                   SongUpdateView,
                   SongDeleteView,
                   SongDetailView,
                   SongListView,
                   song_download_veiw,
                   increase_song_played_view,
                   add_favorite_song_view)
