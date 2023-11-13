from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('create_product', views.create_product, name='create_product'),
    path('your_product_list', views.your_product_list, name='your_product_list'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),

]