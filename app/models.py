from django.db import models
from django.urls import reverse


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    uploaded_date = models.DateTimeField(auto_now=True)
    video_file = models.FileField(upload_to='media/video/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:play", kwargs={"video_id": self.id})
