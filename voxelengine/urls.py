from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'voxelengine'

urlpatterns = [
    path('', voxelengine_index_view, name="index"),
    path('download/installer', download_installer, name='downloade_installer'),
    path('download/', download_page_view, name="download"),
    path('subscriptions/', subscriptions_view, name="subscriptions"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)