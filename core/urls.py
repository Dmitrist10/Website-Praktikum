from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "core"

urlpatterns = [
    path('', index_view, name="index"),
    path('news/', news_view, name="news"),

    path('legal/', legal_view, name="legal"),
    path('legal/terms/', legal_terms_view, name="legal_terms"),
    path('legal/privacy/', legal_privacy_view, name="legal_privacy"),
    path('legal/eula/', legal_eula_view, name="legal_eula"),

    path('showcase/', showcase_view, name="showcase"),
    path('projects/', projects_view, name="projects"),
    
    path('learn/', learn_index_view, name="learn_index"),
    path('learn/engine/', learn_engine_view, name="learn_engine"),
    path('learn/general/', learn_general_view, name="learn_general"),
]
