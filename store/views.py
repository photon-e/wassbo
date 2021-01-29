from django.shortcuts import render , get_object_or_404
from .models import Products , Category

# Create your views here.
def home_view(request):
<<<<<<< HEAD
    return render(request, 'store/index.html', {'home_view': home_view})
=======
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {'products':products,'categories':categories}
    return render(request, 'store/index.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {'product':product}
    return render(request, 'store/product-page.html', context)


>>>>>>> fce40959d6f96589a2b422dbd444a99993ca4c8b
