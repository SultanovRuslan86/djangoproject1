from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'index.html', context=context)
