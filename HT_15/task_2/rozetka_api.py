import requests


class RozetkaAPI(object):
    URL_START = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main?front-type=xl&goodsId='

    def get_item_data(self, product_id):
        """Version with category ID. Could be modified for using category name"""
        request = requests.get(self.URL_START + product_id)
        result = request.json()
        result = result.get('data')
        return self.__result_convert(result)

    @staticmethod
    def __result_convert(result: dict):
        """To match the dict manes described in the task"""
        final_result = dict()
        final_result['item_id'] = result.get('id')
        final_result['title'] = result.get('title')
        final_result['old_price'] = result.get('old_price')
        final_result['current_price'] = result.get('price')
        final_result['href'] = result.get('href')
        final_result['brand'] = result.get('brand')
        final_result['category'] = result.get('category_id')
        return final_result