import os
import csv
import codecs
import shutil
from urllib.request import urlopen
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRobotSite(object):

    def __init__(self):
        self.path = './output'
        self.robot_config_data = []
        self.options = Options()
        self.chrome_options_configure()
        self.driver = webdriver.Chrome(options=self.options)

    def chrome_options_configure(self):
        self.options.add_argument('--start-maximized')
        self.options.add_experimental_option('excludeSwitches', ['disable-popup-blocking', 'enable-automation'])

    def csv_from_url(self):
        """Read the file data from csv url"""
        csv_url = "https://robotsparebinindustries.com/orders.csv"
        response = urlopen(csv_url)
        csv_file = csv.reader(codecs.iterdecode(response, "utf-8"))
        for row in csv_file:
            if row[0] != 'Order number':
                self.robot_config_data.append({'order_number': int(row[0]), 'head': int(row[1]), 'body': int(row[2]),
                                               'legs': int(row[3]), 'address': row[4]})
        print(f'The file from {csv_url} have been read')

    def prepare_folder(self):
        """Create or clear the target folder for data"""
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
            os.mkdir(self.path)
        else:
            os.mkdir(self.path)

    def open_site(self):
        self.driver.get('https://robotsparebinindustries.com/')

    def order_tab(self):
        """Go to the order tab"""
        order_tab = self.driver.find_elements(by=By.CLASS_NAME, value='nav-link')[-1]
        current_condition = EC.element_to_be_clickable(order_tab)
        WebDriverWait(self.driver, 20).until(current_condition).click()

    def close_pop_up(self):
        ok_button = self.driver.find_element(by=By.CLASS_NAME, value='btn-dark')
        current_condition = EC.element_to_be_clickable(ok_button)
        WebDriverWait(self.driver, 20).until(current_condition).click()

    def head_selection(self):
        select_heads = self.driver.find_elements(by=By.CSS_SELECTOR, value='option')
        current_condition = EC.element_to_be_clickable((select_heads[self.order_unit['head']]))
        WebDriverWait(self.driver, 20).until(current_condition).click()

    def body_selection(self):
        select_body = self.driver.find_elements(by=By.CSS_SELECTOR, value='div.stacked input')
        current_condition = EC.element_to_be_clickable((select_body[self.order_unit['body'] - 1]))
        WebDriverWait(self.driver, 20).until(current_condition).click()

    def leg_selection(self):
        input_fields = self.driver.find_elements(by=By.CSS_SELECTOR, value='input.form-control')
        input_fields[0].send_keys(self.order_unit['legs'])

    def address_type(self):
        input_fields = self.driver.find_elements(by=By.CSS_SELECTOR, value='input.form-control')
        input_fields[1].send_keys(self.order_unit['address'])

    def preview_button(self):
        preview_button = self.driver.find_element(by=By.ID, value='preview')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(preview_button)).click()

    def img_save(self):
        """Saving image with the mane "order_number".png to the target folder"""
        robot_image = self.driver.find_element(by=By.ID, value='robot-preview-image')
        current_condition = EC.visibility_of_element_located((By.CSS_SELECTOR, 'div img'))
        WebDriverWait(self.driver, 20).until(current_condition)
        robot_image.screenshot(f'{self.path}/robot_{self.order_unit["order_number"]}.png')

    def order(self):
        """Order the robot and rename the image regarding to the requirements"""
        order_button = self.driver.find_element(by=By.ID, value='order')
        current_condition = EC.element_to_be_clickable(order_button)
        WebDriverWait(self.driver, 20).until(current_condition).click()
        check_number = self.driver.find_element(by=By.CSS_SELECTOR, value='p.badge-success').text
        os.replace(f'{self.path}/robot_{self.order_unit["order_number"]}.png', f'{self.path}/{check_number}_robot.png')
        print(f'The robot {check_number} image saved!')

    def order_another(self):
        """Next robot configuration start"""
        order_another = self.driver.find_element(by=By.ID, value='order-another')
        current_condition = EC.element_to_be_clickable(order_another)
        WebDriverWait(self.driver, 20).until(current_condition).click()

    def check_error_order(self):
        """Exception loop if server error at the order"""
        print('Ordering the robot')
        try:
            self.order()
        except NoSuchElementException:
            print('Server error, retrying to make the order')
            self.check_error_order()

    def configure_robot(self):
        """The whole procedure of the one unit of robot configuration"""
        self.close_pop_up()
        self.head_selection()
        self.body_selection()
        self.leg_selection()
        self.address_type()
        self.preview_button()
        self.img_save()
        self.check_error_order()

    def config_iteration(self):
        """Iteration via all robot configurations listed in csv file"""
        for robot in self.robot_config_data:
            self.order_unit = robot
            self.configure_robot()
            self.order_another()
        print('Ordering the list of robots finished.')


if __name__ == '__main__':
    test_site = TestRobotSite()
    test_site.csv_from_url()
    test_site.prepare_folder()
    test_site.open_site()
    test_site.order_tab()
    test_site.config_iteration()


