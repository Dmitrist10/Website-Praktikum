from django.shortcuts import render

# Create your views here.
def voxelengine_index_view(request):
    return render(request, 'voxelengine/voxelengine_index.html')
