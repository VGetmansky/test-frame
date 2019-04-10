import crm.data.authorization_data as data
import common_functions as additional
from selenium.webdriver.common.by import By
import time


def open_url(driver, url):
    driver.get(url)
    # driver.find_element(By.ID, data.page_id)
    assert ("Users", driver.title)


def add_field(driver, value, field):
    username_field = driver.find_element(By.NAME, field)
    username_field.clear()
    username_field.send_keys(value)


def add_credentials(driver, username, password):
    add_field(driver, username, data.username_el)
    add_field(driver, password, data.password_el)


def submit_form(driver):
    driver.find_element(By.XPATH, data.submit).click()


def verify_url(driver, url):
    assert (url + data.expected_url) == driver.current_url and ("Home", driver.title)


def logout(driver):
    time.sleep(1)
    additional.wait_element(driver, data.account_menu_id, 'id')
    driver.find_element(By.ID, data.account_menu_id).click()
    time.sleep(1)
    additional.wait_element(driver, data.logout_button_id, 'id')
    driver.find_element(By.ID, data.logout_button_id).click()


def verify_logout(driver):
    assert ("Users", driver.title)
