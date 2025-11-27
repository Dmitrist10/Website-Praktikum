from django import forms
from .models import DocumentationPage, DocumentationCategory

class DocumentationCategoryForm(forms.ModelForm):
    class Meta:
        model = DocumentationCategory
        fields = ['title', 'slug', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DocumentationPageForm(forms.ModelForm):
    class Meta:
        model = DocumentationPage
        fields = ['category', 'parent', 'title', 'slug', 'content', 'order']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 20, 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }
