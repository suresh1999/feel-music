from django.contrib import admin
from .models import Album, Lyricist, Song

# Register your models here.
class SongInline(admin.StackedInline):
    model = Song

class AlbumAd(admin.ModelAdmin):
    inlines = [
        SongInline,
    ]
admin.site.register(Album, AlbumAd)
admin.site.register(Lyricist)
admin.site.register(Song)