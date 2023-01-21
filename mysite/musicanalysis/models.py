from django.db import models

# Create your models here.
class PlaylistIdModel(models.Model):
    playlist_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
