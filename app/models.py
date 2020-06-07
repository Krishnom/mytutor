from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Video(models.Model):
    uuid   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='media/video/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.video_file.url
