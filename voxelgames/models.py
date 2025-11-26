from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    price = models.IntegerField(default=0, help_text="Price in Voxels")

    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    version = models.CharField(max_length=255)

    def __str__(self):
        return self.title
