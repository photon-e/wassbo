from django.shortcuts import render , get_object_or_404 
from .models import *

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

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items =[]
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)



def checkout_summary(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items =[]
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout-page.html', context)
