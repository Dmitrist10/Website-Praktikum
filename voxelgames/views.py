from django.shortcuts import render

# Create your views here.
def voxelgames_index_view(request):
    return render(request, 'voxelgames/voxelgames_index.html')
