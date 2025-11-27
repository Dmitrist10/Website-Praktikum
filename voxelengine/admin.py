from django.contrib import admin
from .models import DocumentationCategory, DocumentationPage

# Register your models here.
admin.site.register(DocumentationCategory)
admin.site.register(DocumentationPage)