from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'voxelengine'

urlpatterns = [
    path('', voxelengine_index_view, name="index"),
    path('download/installer', download_installer, name='download_installer'),
    path('download/', download_page_view, name="download"),
    path('subscriptions/', subscriptions_view, name="subscriptions"),

    path('docs/', docs_index, name='docs_index'),
    path('docs/manage/', docs_manage_list, name='docs_manage_list'),
    path('docs/manage/create/', docs_manage_create, name='docs_manage_create'),
    path('docs/manage/edit/<int:pk>/', docs_manage_edit, name='docs_manage_edit'),
    path('docs/manage/delete/<int:pk>/', docs_manage_delete, name='docs_manage_delete'),
    
    path('docs/manage/categories/', docs_manage_category_list, name='docs_manage_category_list'),
    path('docs/manage/categories/create/', docs_manage_category_create, name='docs_manage_category_create'),
    path('docs/manage/categories/edit/<int:pk>/', docs_manage_category_edit, name='docs_manage_category_edit'),
    path('docs/manage/categories/delete/<int:pk>/', docs_manage_category_delete, name='docs_manage_category_delete'),

    path('docs/manage/reorder/', docs_manage_reorder, name='docs_manage_reorder'),

    path('docs/<slug:category_slug>/<slug:page_slug>/', docs_page, name='docs_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)