from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'voxelgames'

urlpatterns = [
    path('', voxelgames_index_view, name="index"),
    path('voxelgames_notLogined/', voxelgames_notLogined_view, name="not_logined"),
    path('store/', store_view, name="store"),
]
