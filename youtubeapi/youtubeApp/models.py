from django.db import models

# Create your models here.
class VideoDetail(models.Model):
    video_id = models.CharField(max_length=50, primary_key=True)
    # published_at = models.DateTimeField()
    video_title = models.CharField(blank=False, max_length=2000)
    video_desc = models.CharField(blank=False, max_length=2000)
    # thumbnail_url = models.URLField()
