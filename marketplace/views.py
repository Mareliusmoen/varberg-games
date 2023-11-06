from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Set the seller to the current user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'marketplace/create_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'marketplace/product_detail.html', {'product': product})