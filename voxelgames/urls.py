from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', voxelgames_index_view, name="index")
]
