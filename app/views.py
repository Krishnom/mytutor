from django.shortcuts import render, get_object_or_404, redirect

from .forms import VideoUploadForm
from .models import Video


def list_available_videos_view(request, *args, **kwargs):
    videos = Video.objects.all
    context = {
        "videos": videos
    }
    return render(request, "video/list.html", context)


def upload_video_view(request, *args, **kwargs):
    form = VideoUploadForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('app:list')
        else:
            form = VideoUploadForm()

    return render(request, "video/upload.html", {"form": form})


def play_video_view(request, id):
    # video = Video.objects.get(id=video_id)
    video = get_object_or_404(Video, id=id)
    return render(request, 'video/play.html', {"video": video})
