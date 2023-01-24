from django.urls import path

from . import views


urlpatterns = [
    path('', views.add_products, name='add_products'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.single_product_view, name='product'),
]