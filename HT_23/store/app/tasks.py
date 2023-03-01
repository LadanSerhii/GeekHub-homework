from celery import shared_task

from app.models import Product, ProductList, ProductCategory
from store.celery import app

import rozetka_api


@shared_task(name='scrape_products', queue='celery')
def scrape_products():
    product_list = str(ProductList.objects.all()[0].product_list)
    product_ids = product_list.split(',')
    ProductList.objects.all().delete()
    for product_id in product_ids:
        get_product.delay(product_id)


@app.task(name='get_product', queue='celery')
def get_product(product_id):
    api = rozetka_api.RozetkaAPI()
    product = api.get_item_data(str(product_id))
    current_category = ProductCategory.objects.get(category_id=product['category'])
    active_product, created = Product.objects.update_or_create(
        title=product['title'],
        old_price=product['old_price'],
        current_price=product['current_price'],
        href=product['href'],
        brand=product['brand'],
        category=product['category'],
        product_category=current_category,
    )