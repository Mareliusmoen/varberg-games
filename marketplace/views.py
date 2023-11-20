from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm
from mtgsdk import Card
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def create_product(request):
    """
    Create a new product based on the given request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)

            # Get the category instance based on the selected category string
            category_str = form.cleaned_data['category']
            category_instance = Category.objects.get(name=category_str)

            # Assign the category instance to the product
            product.category = category_instance

            # Set the seller to the current user
            product.seller = request.user

            # Add card_name handling here
            card_name = form.cleaned_data['card_name']
            if card_name:
                # Handle card search and API request here
                api_url = 'https://api.magicthegathering.io/v1/cards'
                params = {'name': card_name}
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    card_data = response.json()
                    if 'cards' in card_data and len(card_data['cards']) > 0:
                        # Fetch the first card's data
                        card = card_data['cards'][0]
                        # Set the card data in the product
                        product.card_name = card['name']
                        product.card_image_url = card['imageUrl']

            # Save the product after card handling
            product.save()
            messages.success(
                request, 'Your item was listed for sale successfully.')
            # Redirect to product_list after successfully saving the product
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'marketplace/create_product.html', {'form': form})


def edit_product(request, product_id):
    """
    Edit a product.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to be edited.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the product with the given ID does not exist.
    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)

            # Get the category instance based on the selected category string
            category_str = form.cleaned_data['category']
            category_instance = Category.objects.get(name=category_str)

            # Assign the category instance to the product
            product.category = category_instance

            # Set the seller to the current user
            product.seller = request.user

            # Add card_name handling here
            card_name = form.cleaned_data['card_name']
            if card_name:
                # Handle card search and API request here
                api_url = 'https://api.magicthegathering.io/v1/cards'
                params = {'name': card_name}
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    card_data = response.json()
                    if 'cards' in card_data and len(card_data['cards']) > 0:
                        # Fetch the first card's data
                        card = card_data['cards'][0]
                        # Set the card data in the product
                        product.card_name = card['name']
                        product.card_image_url = card['imageUrl']

            # Save the product after card handling
            product.save()
            messages.success(request, 'Your item was updated successfully.')
            # Redirect to product_list after successfully saving the product
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(
        request, 
        'marketplace/edit_product.html', 
        {'form': form, 'product': product}
    )

def product_list(request):
    """
    Renders the 'product_list.html' template with a list of all products.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTTP response.
    """
    products = Product.objects.all()
    return render(
        request,
        'marketplace/product_list.html',
        {'products': products}
    )


def product_detail(request, product_id):
    """
    Renders the product detail page for a given product ID.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product.

    Returns:
        HttpResponse: The rendered product detail page.
    """
    product = get_object_or_404(Product, id=product_id)
    return render(
        request, 'marketplace/product_detail.html', {'product': product})


@login_required
def your_product_list(request):
    """
    Renders the user's product list.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template with the user's product list.
    """
    products = Product.objects.filter(seller=request.user)
    return render(
        request, 'marketplace/your_product_list.html', {'products': products})


@login_required
def delete_product(request, product_id):
    """
    Deletes a product.

    Parameters:
        - request: The HTTP request object.
        - product_id: The ID of the product to be deleted.

    Returns:
        - Redirects to the login page if the user is not authenticated.
        - Deletes the product if the user is the seller.
        - Redirects to the product list page.
    """
    # Check if the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page

    # Get the product by ID
    product = get_object_or_404(Product, id=product_id)

    # Check if the user is the seller of the product
    if request.user == product.seller:
        # Delete the event
        product.delete()
    messages.success(
        request, "You have successfully deleted the item for 	sale.")
    return redirect('your_product_list')


@csrf_exempt
def product_sold(request):
    """
    This function handles the request to mark a product as sold.
    It expects a POST request with the product ID as a parameter.
    If the product exists, it updates the 'sold' attribute of the product to
    True and returns a JSON response with {"success": True}. If product does
    not exist, it returns a JSON response with {"success": False, "error":
    "Product does not exist"}. If the request method is not POST, it returns a
JSON response with {"success": False, "error": "Invalid request"}.

    Parameters:
    - request: The request object containing the HTTP request data.

    Returns:
    - JsonResponse: A JSON response with the success status and, in case of
    failure, an error message.
    """
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            product.sold = True
            product.save()
            return JsonResponse({"success": True})
        except Product.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Product does not exist"})
    else:
        return JsonResponse({"success": False, "error": "Invalid request"})
