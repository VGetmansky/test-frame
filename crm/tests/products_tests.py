from crm.data import authorization_data as auth_data, products_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def click_all_category(driver):
    additional.select_category_all(driver)


def select_products_category(driver, url):
    additional.wait_element(driver, data.products_category_id, 'id')
    driver.find_element(By.ID, data.products_category_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Products", driver.title)


def click_add_product(driver, url):
    additional.wait_element(driver, data.add_product_id, 'id')
    driver.find_element(By.ID, data.add_product_id).click()
    assert (url + data.expected_product_url) == driver.current_url
