from django.urls import path

from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('delete/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('clear/', views.cart_clear, name='cart_clear'),
    path('ajax_cart_clear/', views.CartClearView.as_view(template_name='cart.html'), name='ajax_cart_clear'),
]