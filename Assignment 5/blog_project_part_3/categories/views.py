from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        category_from= forms.CategoryForm(request.POST)
        if category_from.is_valid():
            category_from.save()
            return redirect('add_category')
    else:
        category_from= forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_from})