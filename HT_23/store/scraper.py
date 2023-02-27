import os
import sys

import django
django.setup()
from app.models import Product, ProductList, ProductCategory

import rozetka_api


sys.path.append(os.path.abspath(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rozetka_products.settings')

api = rozetka_api.RozetkaAPI()
product_list = str(ProductList.objects.all()[0].product_list)
product_ids = product_list.split(',')
ProductList.objects.all().delete()
for product_id in product_ids:
    try:
        product = api.get_item_data(str(product_id))
        if Product.objects.filter(item_id=product_id):
            current_category = ProductCategory.objects.get(category_id=product['category'])
            current_product = Product.objects.filter(item_id=product_id).update(
                title=product['title'],
                old_price=product['old_price'],
                current_price=product['current_price'],
                href=product['href'],
                brand=product['brand'],
                category=product['category'],
                product_category=current_category,
            )
        else:
            current_category = ProductCategory.objects.get(category_id=product['category'])
            new_product = Product(
                item_id=product_id,
                title=product['title'],
                old_price=product['old_price'],
                current_price=product['current_price'],
                href=product['href'],
                brand=product['brand'],
                category=product['category'],
                product_category=current_category
            )
            new_product.save()
    except Exception:
        pass



