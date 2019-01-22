from django.db import models
from datetime import datetime
# Create your models here.

def album_img(instance,filename):
    return '{} {}'.format(datetime.now(), filename)
class Album(models.Model):
    name = models.CharField(blank=False, max_length=40)
    img = models.ImageField(upload_to=album_img,)
    released_on = models.DateField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    trend = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Lyricist(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    bio = models.CharField(max_length=1000)

class Song(models.Model):
    name = models.CharField(blank=False, max_length=60)
    released_on = models.DateField()
    meaning = models.TextField(max_length=3000)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    written_by = models.ForeignKey(Lyricist)
    added_on = models.DateField(auto_now_add=True)
    download_link = models.URLField()
    video_link = models.URLField()
    trend = models.IntegerField(default=0)

