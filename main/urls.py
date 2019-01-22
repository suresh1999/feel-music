from django.conf.urls import url
from django.views.generic import TemplateView,DetailView,ListView
from .views import AlbumView, AlbumListView, SearchView, HomePageView
from .models import Song
urlpatterns = [
    url('^songs/$', ListView.as_view(model=Song, template_name='index.html', queryset=Song.objects.all()),name='songs'),
    url('^songs/(?P<pk>\d+)/$', DetailView.as_view(model=Song, template_name='contents.html',queryset=Song.objects.all()), name='song-detail'),
    url('^albums/(?P<aid>\d+)/$', AlbumView.as_view(),  name='album_list'),
    url('^albums/$', AlbumListView.as_view(), name='albums'),
    url('^search/$', SearchView, name='search'),
    url('^$', HomePageView, name="index"),
]