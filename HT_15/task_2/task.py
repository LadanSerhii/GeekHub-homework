import data_operations as data_op
import rozetka_api

path = input('Please enter the path to .csv file with Rozetka products ID: ')
r_data = data_op.CsvOperations(path)
w_data = data_op.DataBaseOperations()
try:
    id_list = r_data.read_csv()
    print(id_list)
    api = rozetka_api.RozetkaAPI()
    for product_id in id_list:
        try:
            print(product_id)
            product = api.get_item_data(product_id)
            w_data.write_to_db(product)
            print(f'The data for ID {product_id} successfully added to database!')
        except Exception:
            print(f'Invalid product ID {product_id} or could not extract data from website!')
except Exception:
    print('File error!')











