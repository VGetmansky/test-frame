import os, sys
from selenium.webdriver.common.by import By

from crm.data import reports_data as data, authorization_data as auth_data, values_data as values, quotes_data as qdata
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


def select_invoice(driver):
    driver.get("https://crmtst.bai-inc.eu/index.php?module=Invoice&view=List")
    assert "Invoice", driver.title and driver.current_url == "https://crmtst.bai-inc.eu/index.php?module=Invoice&view=List"


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
    additional.select_table_cell(driver, data.first_po_cell_id, "po", url)


def open_invoice_details(driver, url):
    time.sleep(2)
    additional.wait_element(driver, data.first_invoice_cell_id, 'id')
    additional.select_table_cell(driver, data.first_invoice_cell_id, "invoice", url)


def expand_pdfmaker(driver):
    time.sleep(2)
    if driver.title == "Invoice":
        additional.wait_element(driver,"//h5[contains(., 'PDFMaker')]", 'xpath')
        driver.find_element(By.XPATH, "//h5[contains(., 'PDFMaker')]").click()
    else:
        additional.wait_element(driver, data.pdfmaker_tab, 'xpath')
        additional.click_element_by_xpath(driver, data.pdfmaker_tab)
    # additional.click_element_by_xpath(driver, data.edit_and_export)


def export_document(driver):
    global path
    path = os.path.expanduser(os.getenv('HOME')) + "/Downloads"  # Путь к вашей папке
    doc_len = len([name for name in os.listdir(path)])
    additional.click_element_by_xpath(driver, data.export)

    i = 0
    n = 0
    while (i < 20):
        if len([name for name in os.listdir(path)]) == doc_len:

            time.sleep(1)
            i += 1
        else:
            while n != 1:
                # Получим список имен всего содержимого папки
                # и превратим их в абсолютные пути
                dir_list = [os.path.join(path, x) for x in os.listdir(path)]

                if dir_list:
                    # Создадим список из путей к файлам и дат их создания.
                    date_list = [[x, os.path.getctime(x)] for x in dir_list]

                    # Отсортируем список по дате создания в обратном порядке
                    sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

                    # Выведем первый элемент списка. Он и будет самым последним по дате

                    if len((sort_date_list[0][0]).split('.')) != 2:
                        time.sleep(1)
                    else:
                        global pdf
                        pdf = (sort_date_list[0][0])
                        print(sort_date_list[0][0])
                        i = 20
                        n = 1


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


def select_report_type(driver, type, territory, module):
    deselect_reports(driver, territory, module)

    if type == "so_bann_proforma":
        value = "//option[contains(., 'BANN - Proforma')]"

    elif type == "so_bann_salesorder":
        value = "//option[contains(., 'BANN - SalesOrder')]"

    elif type == "so_bai_proforma":
        value = "//option[contains(., 'BAI - Proforma')]"

    elif type == "so_bai_salesorder":
        value = "//option[contains(., 'BAI - SalesOrder')]"

    elif type == "i_bai_customs_invoice":
        value = "//option[contains(., 'BAI - Customs Invoice')]"

    elif type == "i_bai_invoice":
        value = "//option[contains(., 'BAI - Invoice')]"

    elif type == "i_bai_packing_list":
        value = "//option[contains(., 'BAI - Packing List')]"

    elif type == "i_bann_customs_invoice":
        value = "//option[contains(., 'BANN - Customs Invoice')]"

    elif type == "i_bann_invoice":
        value = "//option[contains(., 'BANN - Invoice')]"

    elif type == "i_bann_packing_list":
        value = "//option[contains(., 'BANN - Packing List')]"

    driver.find_element(By.XPATH, value).click()

    if driver.find_element(By.XPATH, value).get_property('selected') is False:
        driver.find_element(By.XPATH, value).click()
    else:
        return


def deselect_reports(driver, territory, module):
    if territory == "bann-i" or territory == "bann-d":

        if module == "SO":

            if driver.find_element(By.XPATH, "//option[contains(., 'BANN - Proforma')]").get_property('selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BANN - Proforma')]").click()

            elif driver.find_element(By.XPATH, "//option[contains(., 'BANN - SalesOrder')]").get_property('selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BANN - SalesOrder')]").click()

            else:
                return

        elif module == "Invoice":

            if driver.find_element(By.XPATH, "//option[contains(., 'BANN - Invoice')]").get_property('selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BANN - Invoice')]").click()

            elif driver.find_element(By.XPATH, "//option[contains(., 'BANN - Customs Invoice')]").get_property('selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BANN - Customs Invoice')]").click()

            elif driver.find_element(By.XPATH, "//option[contains(., 'BANN - Packing List')]").get_property('selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BANN - Packing List')]").click()

            else:
                return

    elif territory =="ees":

        if module == "SO":

            if driver.find_element(By.XPATH, "//option[contains(., 'BAI - Proforma')]").get_property('selected') is True:
                driver.find_element(By.XPATH,"//option[contains(., 'BAI - Proforma')]").click()

            elif driver.find_element(By.XPATH, "//option[contains(., 'BAI - SalesOrder')]").get_property('selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BAI - SalesOrder')]").click()
            else:
                return

        elif module == "Invoice":

            if driver.find_element(By.XPATH, "//option[contains(., 'BAI - Invoice')]").get_property(
                    'selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BAI - Invoice')]").click()

            elif driver.find_element(By.XPATH, "//option[contains(., 'BAI - Customs Invoice')]").get_property(
                    'selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BAI - Customs Invoice')]").click()

            elif driver.find_element(By.XPATH, "//option[contains(., 'BAI - Packing List')]").get_property(
                    'selected') is True:
                driver.find_element(By.XPATH, "//option[contains(., 'BAI - Packing List')]").click()
            else:
                return
