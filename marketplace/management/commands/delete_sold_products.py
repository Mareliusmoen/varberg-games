from datetime import date
from django.utils import timezone
from marketplace.models import Product

def delete_sold_products():
    current_date = date.today()

    # filter the database for products marked as sold
    sold_products = Product.objects.filter(sold=True)

    # Loop through the sold products and delete them if they are older than selected timeframe
    for product in sold_products:
        if product.created_at.date() < current_date:
            product.delete()

if __name__ == '__main__':
    delete_sold_products()