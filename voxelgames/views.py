from django.shortcuts import render, redirect

# Create your views here.
def voxelgames_index_view(request):
    if not request.user.is_authenticated:
        return redirect('voxelgames:not_logined')
    return render(request, 'voxelgames/voxelgames_index.html')

def voxelgames_notLogined_view(request):
    return render(request, 'voxelgames/voxelgames_notLogined.html')
