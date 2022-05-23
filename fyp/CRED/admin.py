from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Videos)
admin.site.register(Audios)
admin.site.register(Books)
admin.site.register(Quotes)
admin.site.register(video_playlist)
admin.site.register(audio_playlist)
admin.site.register(video_history)