from django.urls import path

from .views import SongView


urlpatterns = [
    path("play/song/<int:pk>/", SongView.as_view(), name="song")
]
