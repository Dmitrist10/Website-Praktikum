from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'core/core_index.html')

def news_view(request):
    return render(request, 'core/news.html')

def legal_view(request):
    return render(request, 'core/legal.html')

def legal_terms_view(request):
    return render(request, 'core/legal_terms.html')

def legal_privacy_view(request):
    return render(request, 'core/legal_privacy.html')

def legal_eula_view(request):
    return render(request, 'core/legal_eula.html')