# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 18:19
from __future__ import unicode_literals

from django.db import migrations

videos = (
    # Sample videos
    "https://www.youtube.com/watch?v=IzbCLooj-M8",
    "https://www.youtube.com/watch?v=9V6BDnu35qs",
    "https://www.youtube.com/watch?v=R1JBQMXbN2k",
    "https://www.youtube.com/watch?v=41Zjh3AirjU",
    "https://www.youtube.com/watch?v=lsSC2vx7zFQ",
    "https://www.youtube.com/watch?v=vIq07-f2aqc",
)


def create_default_videos(apps, schema):
    MotivationalVideo = apps.get_model("reporter", "MotivationalVideo")
    for video_url in videos:
        motivational_video = MotivationalVideo(url=video_url)
        motivational_video.save()


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_videos)
    ]