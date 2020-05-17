"""mytutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import list_available_videos_view, upload_video_view, play_video_view
app_name = "app"
urlpatterns = [
    path("", list_available_videos_view, name="home"),
    path("list/", list_available_videos_view, name="list"),
    path("upload/", upload_video_view, name="upload"),
    path("play/<int:id>", play_video_view, name="play"), ]
