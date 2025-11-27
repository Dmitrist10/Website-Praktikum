from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
import os
import json
from .models import DocumentationCategory, DocumentationPage
from .forms import DocumentationPageForm, DocumentationCategoryForm

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

def download_page_view(request):
    return render(request, 'voxelengine/download.html')

def subscriptions_view(request):
    return render(request, 'voxelengine/subscriptions.html')

# --- Documentation Views ---

def docs_index(request):
    categories = DocumentationCategory.objects.prefetch_related('pages').all()
    first_page = DocumentationPage.objects.first()
    if first_page:
        return redirect('voxelengine:docs_page', category_slug=first_page.category.slug, page_slug=first_page.slug)
    return render(request, 'voxelengine/docs/base_docs.html', {'categories': categories})

def docs_page(request, category_slug, page_slug):
    categories = DocumentationCategory.objects.prefetch_related('pages').all()
    page = get_object_or_404(DocumentationPage, category__slug=category_slug, slug=page_slug)
    return render(request, 'voxelengine/docs/page.html', {
        'categories': categories,
        'current_page': page,
        'current_category': page.category
    })

# --- Documentation Management Views ---

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def docs_manage_list(request):
    pages = DocumentationPage.objects.all()
    return render(request, 'voxelengine/docs/manage_list.html', {'pages': pages})

@user_passes_test(is_staff)
def docs_manage_create(request):
    if request.method == 'POST':
        form = DocumentationPageForm(request.POST)
        if form.is_valid():
            page = form.save()
            return redirect('voxelengine:docs_page', category_slug=page.category.slug, page_slug=page.slug)
    else:
        form = DocumentationPageForm()
    return render(request, 'voxelengine/docs/manage_form.html', {'form': form, 'title': 'Create Page'})

@user_passes_test(is_staff)
def docs_manage_edit(request, pk):
    page = get_object_or_404(DocumentationPage, pk=pk)
    if request.method == 'POST':
        form = DocumentationPageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            return redirect('voxelengine:docs_page', category_slug=page.category.slug, page_slug=page.slug)
    else:
        form = DocumentationPageForm(instance=page)
    return render(request, 'voxelengine/docs/manage_form.html', {'form': form, 'title': 'Edit Page'})

@user_passes_test(is_staff)
def docs_manage_delete(request, pk):
    page = get_object_or_404(DocumentationPage, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('voxelengine:docs_manage_list')
    return render(request, 'voxelengine/docs/manage_delete.html', {'page': page})

@user_passes_test(is_staff)
def docs_manage_category_list(request):
    categories = DocumentationCategory.objects.all()
    return render(request, 'voxelengine/docs/manage_category_list.html', {'categories': categories})

@user_passes_test(is_staff)
def docs_manage_category_create(request):
    if request.method == 'POST':
        form = DocumentationCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voxelengine:docs_manage_category_list')
    else:
        form = DocumentationCategoryForm()
    return render(request, 'voxelengine/docs/manage_category_form.html', {'form': form, 'title': 'Create Category'})

@user_passes_test(is_staff)
def docs_manage_category_edit(request, pk):
    category = get_object_or_404(DocumentationCategory, pk=pk)
    if request.method == 'POST':
        form = DocumentationCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('voxelengine:docs_manage_category_list')
    else:
        form = DocumentationCategoryForm(instance=category)
    return render(request, 'voxelengine/docs/manage_category_form.html', {'form': form, 'title': 'Edit Category'})

@user_passes_test(is_staff)
def docs_manage_category_delete(request, pk):
    category = get_object_or_404(DocumentationCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('voxelengine:docs_manage_category_list')
    return render(request, 'voxelengine/docs/manage_category_delete.html', {'category': category})

@user_passes_test(is_staff)
def docs_manage_reorder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            def update_order(items, parent=None):
                for index, item in enumerate(items):
                    page = DocumentationPage.objects.get(pk=item['id'])
                    page.parent = parent
                    page.order = index
                    page.save()
                    if 'children' in item:
                        update_order(item['children'], parent=page)

            update_order(data)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'invalid method'}, status=405)