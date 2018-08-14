from crm.data import authorization_data as auth_data, material_arrival_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def click_all_category(driver):
    additional.select_category_all(driver)


def select_material_arrival_category(driver, url):
    additional.wait_element(driver, data.material_arrival_id, 'id')
    driver.find_element(By.ID, data.material_arrival_id).click()
    assert (url + data.expected_url) == driver.current_url and ("WHStock", driver.title)
