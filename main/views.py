from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Song, Album
from django.http import HttpResponse
from django.db.models import Q
from .forms import SearchForm
# Create your views here.
class AlbumView(ListView):
    model = Album
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(AlbumView,self).get_context_data(**kwargs)
        album = get_object_or_404(Album, id=int(self.kwargs['aid']))
        context['img'] = album.img
        return context
    def get_queryset(self,*args,**kwargs):
        album = get_object_or_404(Album, id=int(self.kwargs['aid']))
        query = album.song_set.all()
        return query


class AlbumListView(ListView):
    model = Album
    template_name = 'album.html'

def SearchView(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            context = {}
            albums = Album.objects.filter(Q(name__iexact=item)|Q(name__icontains=item))
            a_c = albums.count()
            songs = Song.objects.filter(Q(name__iexact=item)|Q(name__icontains=item))
            s_c = songs.count()
            context['albums'] = albums
            context['songs'] = songs
            context['total'] = a_c + s_c
            return render(request,'search.html', context=context)
    return HttpResponse("You are not allowed to use get request")

def HomePageView(request):
    recent_albums = Album.objects.all().order_by('added_on')[:5]
    trending_albums = Album.objects.all().order_by('-trend')[:5]
    trending_songs = Album.objects.all().order_by('-trend')[:5]
    return render(request,"homepage.html",{"recent_al" : recent_albums, "trend_al" : trending_albums, "trend_so" : trending_songs})