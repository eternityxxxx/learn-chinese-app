from django.contrib import admin

from .models import Song, Timecode


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(Timecode)
class TimecodeAdmin(admin.ModelAdmin):
    pass
