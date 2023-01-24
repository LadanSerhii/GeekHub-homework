from django.urls import path

from . import views


urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('delete/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/clear', views.cart_clear, name='cart_clear'),
]