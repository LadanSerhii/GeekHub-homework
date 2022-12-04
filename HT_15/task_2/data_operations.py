import csv
import sqlite3
import rozetka_api


class CsvOperations(object):

    def __init__(self, path):
        self.path = path

    def read_csv(self):
        """According to the task requirements reading from a file and searching column with 'ID' name"""
        result = []
        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            headings = next(reader)
            col_number = headings.index('ID')
            for row in reader:
                result.append(row[col_number])
        return result


class DataBaseOperations(object):

    def write_to_db(self, data: dict):
        conn = sqlite3.connect('rozetka.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO PRODUCTS (ITEM_ID, TITLE, OLD_PRICE, NEW_PRICE, HREF, BRAND, CATEGORY)
        VALUES(?, ?, ?, ?, ?, ?, ?)''', (data['item_id'], data['title'], data['old_price'], data['current_price'],
                                         data['href'], data['brand'], data['category']))
        conn.commit()
        conn.close()
