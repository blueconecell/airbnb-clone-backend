from django.contrib import admin
from .models import Media, Video

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass