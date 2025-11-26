from django.contrib import admin

# Register your models here.
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'release_date')
    search_fields = ('title',)
