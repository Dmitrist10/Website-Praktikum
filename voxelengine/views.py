from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os


# Create your views here.
def voxelengine_index_view(request):
    return render(request, 'voxelengine/voxelengine_index.html')


def download_installer(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'GameEngine.zip')
    
    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, 'rb'), 
            as_attachment=True, 
            filename='GameEngine.zip'
        )
    else:
        return render(request, 'voxelengine/voxelengine_index.html', status=404)