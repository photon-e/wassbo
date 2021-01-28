from django.shortcuts import render , get_object_or_404
from .models import Products , Category

# Create your views here.
def home_view(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {'products':products,'categories':categories}
    return render(request, 'store/index.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {'product':product}
    return render(request, 'store/product-page.html', context)


