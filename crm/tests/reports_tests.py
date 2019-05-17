import os
from selenium.webdriver.common.by import By

from crm.data import reports_data as data, authorization_data as auth_data, values_data as values
import common_functions as additional
import re, time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def select_quote(driver):
    new_url = driver.current_url
    time.sleep(3)
    if driver.title != "Quotes":
        additional.wait_element_for_click(driver, auth_data.quotes_main_button_id)
        additional.wait_new_page(driver, new_url)
    # assert "Rfq", driver.title and driver.current_url == "http://crmqa.bai-inc.eu/index.php?module=Rfq&view=List"


def select_so(driver):
    new_url = driver.current_url
    time.sleep(3)
    if driver.title != "SO":
        additional.wait_element_for_click(driver, auth_data.so_main_button_id)
        additional.wait_new_page(driver, new_url)
    # assert "Rfq", driver.title and driver.current_url == "http://crmqa.bai-inc.eu/index.php?module=Rfq&view=List"


def select_po(driver):
    new_url = driver.current_url
    time.sleep(3)
    if driver.title != "PO":
        additional.wait_element_for_click(driver, auth_data.po_main_button_id)
        additional.wait_new_page(driver, new_url)
    # assert "Rfq", driver.title and driver.current_url == "http://crmqa.bai-inc.eu/index.php?module=Rfq&view=List"


def open_quote_details(driver, url):
    time.sleep(2)
    additional.wait_element(driver, data.first_quotes_cell_id, 'id')
    additional.select_table_cell(driver, data.first_quotes_cell_id, "quote", url)


def open_so_details(driver, url):
    time.sleep(2)
    additional.wait_element(driver, data.first_so_cell_id, 'id')
    additional.select_table_cell(driver, data.first_so_cell_id, "so", url)


def open_po_details(driver, url):
    time.sleep(2)
    additional.wait_element(driver, data.first_po_cell_id, 'id')
    additional.select_table_cell(driver, data.first_po_cell_id, "so", url)


def expand_pdfmaker(driver):
    additional.click_element_by_xpath(driver, data.pdfmaker_tab)
    # additional.click_element_by_xpath(driver, data.edit_and_export)


def export_document(driver):
    additional.click_element_by_xpath(driver, data.export)

    path = './'  # Путь к вашей папке

    # Получим список имен всего содержимого папки
    # и превратим их в абсолютные пути
    dir_list = [os.path.join(path, x) for x in os.listdir(path)]

    if dir_list:
        # Создадим список из путей к файлам и дат их создания.
        date_list = [[x, os.path.getctime(x)] for x in dir_list]

        # Отсортируем список по дате создания в обратном порядке
        sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

        # Выведем первый элемент списка. Он и будет самым последним по дате
    print (sort_date_list[0][0])
    print("adsas")


# Save and export
def get_body_data(driver):
    driver.execute_script("window.scrollTo(0, 0)")
    try:
        windowhandler = driver.window_handles
        assert ConnectionResetError
    except ConnectionResetError:
        windowhandler = driver.window_handles

    window_before = driver.window_handles[0]

    try:
        elem = driver.find_element(By.ID, data.edit_and_export)
        assert NoSuchElementException
    except NoSuchElementException:

        elem = driver.find_element(By.XPATH, data.edit_and_export)
        assert NoSuchElementException

    elem.click()

    WebDriverWait(driver, 30).until(
        lambda driver: len(windowhandler) != len(driver.window_handles))

    window_after = driver.window_handles[1]

    time.sleep(2)

    driver.switch_to.window(window_after)
    # window 2
    assert driver.title == "PDFMaker"

    driver.find_element(By.ID, data.body_tab_id).click()
    driver.find_element(By.ID, data.header_tab_id).click()
    driver.find_element(By.ID, data.footer_tab_id).click()

    driver.switch_to.window(window_before)
    # window 1
