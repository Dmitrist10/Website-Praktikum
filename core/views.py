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

def showcase_view(request):
    return render(request, 'core/showcase.html')

def projects_view(request):
    return render(request, 'core/projects.html')

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

def showcase_view(request):
    return render(request, 'core/showcase.html')

def projects_view(request):
    return render(request, 'core/projects.html')

def learn_index_view(request):
    return render(request, 'core/learn/index.html')

def learn_engine_view(request):
    return render(request, 'core/learn/engine.html')

def learn_general_view(request):
    return render(request, 'core/learn/general.html')

def career_view(request):
    return render(request, 'core/career.html')