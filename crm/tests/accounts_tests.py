from crm.data import authorization_data as auth_data, accounts_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def select_accounts(driver):
    if driver.title != "Accounts":
        additional.wait_element_for_click(driver, auth_data.accounts_main_button_id)
        # driver.find_element(By.ID, auth_data.accounts_main_button_id).click()
    assert "Accounts", driver.title


def click_add_account(driver, url):
    additional.wait_element(driver, data.add_account_id, 'id')
    driver.find_element(By.ID, data.add_account_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Accounts", driver.title)