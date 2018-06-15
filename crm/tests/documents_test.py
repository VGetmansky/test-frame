from crm.data import authorization_data as auth_data
from selenium.webdriver.common.by import By


def select_documents(driver):
    if driver.title != "Documents":
        driver.find_element(By.ID, auth_data.documents_main_button_id).click()
    assert "Documents", driver.title
