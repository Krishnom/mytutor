from django.shortcuts import render, get_object_or_404, redirect

from .forms import VideoUploadForm, UserLoginForm, UserRegisterForm
from .models import Video
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.decorators import login_required

@login_required
def list_available_videos_view(request, *args, **kwargs):
    videos = Video.objects.all
    context = {
        "videos": videos
    }
    return render(request, "video/list.html", context)

@login_required
def upload_video_view(request, *args, **kwargs):
    form = VideoUploadForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('app:list')
        else:
            form = VideoUploadForm()

    return render(request, "video/upload.html", {"form": form})

@login_required
def play_video_view(request, id):
    # video = Video.objects.get(id=video_id)
    video = get_object_or_404(Video, uuid=id)
    return render(request, 'video/play.html', {"video": video})


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def signup_view(request):
    next_url = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        if next_url:
            return redirect(next_url)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
