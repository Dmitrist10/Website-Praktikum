from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'voxelengine'

urlpatterns = [
    path('', voxelengine_index_view, name="index"),
    path('download/installer', download_installer, name='downloade_installer'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)