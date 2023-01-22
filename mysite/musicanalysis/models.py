from django.db import models

class PlaylistUrlModel(models.Model):
    playlist_url = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
