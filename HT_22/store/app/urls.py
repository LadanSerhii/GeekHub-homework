from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('product-category', views.ProductCategoryView)
router.register('product', views.ProductView)
router.register('product-list', views.ProductListView)

urlpatterns = [
    path('', views.add_products, name='add_products'),
    path('products/', views.products, name='products'),
    path('category/<int:category_id>/', views.category_view, name='category_filter'),
    path('products/<int:product_id>/', views.single_product_view, name='product'),
    path('delete/<int:product_id>/', views.delete_view, name='delete'),
    path('update/<int:product_id>/', views.update_view, name='update'),
    path('create/', views.create_view, name='create'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('api/', include(router.urls)),
]