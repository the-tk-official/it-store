from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('product/<int:product_id>', view_product, name='view_product'),
    path('product/add-product', add_product, name='add_product')
]