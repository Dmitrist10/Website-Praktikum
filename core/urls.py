from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "core"

urlpatterns = [
    path('', index_view, name="index"),
    path('news/', news_view, name="news"),
    path('legal/', legal_view, name="legal"),
]
