import data_operations as data_op
import rozetka_api


print('START')
file_path = input('Please enter the path to .csv file with Rozetka products ID: ')
r_data = data_op.CsvOperations(file_path)
w_data = data_op.DataBaseOperations()
try:
    id_list = r_data.read_csv()
    api = rozetka_api.RozetkaAPI()
    for product_id in id_list:
        try:
            product = api.get_item_data(product_id)
            print(f'Product {product_id} successfully added to database!')
            try:
                w_data.write_to_db(product)
            except Exception:
                print('Database error!')
        except Exception:
            print(f'Invalid product ID {product_id} or could not extract data from website!')
except Exception:
    print('csv file error!')

