import crm.data.common_data as data
import time
import string
import datetime
import math
import random
import socket
import errno

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from crm.data import rfq_data, quotes_data, po_data, so_data, authorization_data


def get_name():
    curdate = str(datetime.datetime.now()).split('.')[0]
    val = len(str(datetime.datetime.now()).split('.')[0])
    i = 0
    s = ''
    while i < val:
        if curdate[i].isdigit():
            s += str(curdate[i])
            i += 1
        else:
            i += 1
    name = int(math.sqrt(math.sqrt(int(s) * random.randint(2, 5))))
    return name


def select_first_cell(driver, element_id, account):
    try:
        windowhandler = driver.window_handles
        assert ConnectionResetError
    except ConnectionResetError:
        windowhandler = driver.window_handles

    window_before = driver.window_handles[0]

    try:
        elem = driver.find_element(By.ID, element_id)
        assert NoSuchElementException
    except NoSuchElementException:

        elem = driver.find_elements(By.XPATH, element_id)
        assert NoSuchElementException
        elem = elem[1]
    elem.click()

    WebDriverWait(driver, 30).until(
        lambda driver: len(windowhandler) != len(driver.window_handles))

    window_after = driver.window_handles[1]

    time.sleep(2)  # crutch remake it later

    WebDriverWait(driver, 10).until(
        lambda driver: driver.title != "New Tab"
    )

    time.sleep(0.2)
    driver.switch_to.window(window_after)
    while len(driver.window_handles) != 1:
        i = 1
        while i <= 9:

            if driver.title == "Accounts":
                wait_element(driver, data.search_value_id, 'id')
                driver.find_element(By.ID, data.search_value_id).send_keys("Account for autotests")
                wait_element(driver, data.search_value_button_id, 'id')
                driver.find_element(By.ID, data.search_value_button_id).click()

                try:
                    wait_element(driver, data.first_account_row_id, 'id')
                    wait = WebDriverWait(driver, 10)
                    wait.until(EC.invisibility_of_element_located((By.ID, data.check_account_row_id)))
                    global gaccount
                    gaccount = str(wait_element(driver, data.first_account_row_id, 'id').get_attribute("data-name"))
                    click_element_by_id(driver, data.first_account_row_id)
                    i = 10
                except:
                    i = i

            elif driver.title == "Sales Order":
                global gsales
                gsales = str(wait_element(driver, data.first_product_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_product_row_id)
                i = 10

            elif driver.title == "Purchase Order":
                global gpurchaseorder
                gpurchaseorder = str(wait_element(driver, data.first_po_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_po_row_id)
                i = 10

            elif driver.title == "Vendors":
                global gvendor
                gvendor = str(wait_element(driver, data.first_vendor_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_vendor_row_id)
                i = 10

            elif driver.title == "Quotes":
                global gquote
                gquote = str(wait_element(driver, data.first_quote_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_quote_row_id)
                i = 10

            elif driver.title == "Contacts":
                global gcontacts
                gcontacts = str(wait_element(driver, data.first_contact_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_contact_row_id)
                i = 10

            elif driver.title == "Fleet":
                global gfleet
                gfleet = str(wait_element(driver, data.first_fleet_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_fleet_row_id)
                i = 10

            elif driver.title == "Locations":
                global glocation
                glocation = str(wait_element(driver, data.first_location_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_location_row_id)
                i = 10

            elif driver.title == "Relationships":
                global grelationship
                grelationship = str(wait_element(driver, data.first_relationship_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_relationship_row_id)
                i = 10

            elif driver.title == "Users":
                global guser
                guser = str(wait_element(driver, data.first_user_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_user_row_id)
                i = 10

            elif driver.title == "Assets":
                global gasset
                gasset = str(wait_element(driver, data.first_asset_row_id, 'id').get_attribute("data-name"))
                click_element_by_id(driver, data.first_asset_row_id)
                i = 10

            else:
                time.sleep(0.3)
                i += 1

    driver.switch_to.window(window_before)

    # WebDriverWait(driver, 30).until(
    #     lambda driver: len(driver.window_handles) == 1)
    #    wait.until(lambda driver: driver.getWindowHandles().size() == 1)
    if account is True:
        click_element_by_xpath(driver, data.no_dialog_button)
    else:
        return


def click_element_by_id(driver, value):
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.element_to_be_clickable((By.ID, value)))
    builder = ActionChains(driver)
    builder.move_to_element(elem).click(elem).perform()


def click_element_by_xpath(driver, value):
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, value)))
    builder = ActionChains(driver)
    builder.move_to_element(elem).click(elem).perform()


def fill_text_field(driver, value, text):
    try:
        wait_element(driver, value, 'id')
        elem = driver.find_element(By.ID, value)
        assert NoSuchElementException
    except:
        wait_element(driver, value, 'xpath')
        elem = driver.find_element(By.XPATH, value)
        assert NoSuchElementException
    elem_before = elem.get_attribute("value")

    elem.click()
    elem.send_keys(Keys.CONTROL + "a")
    #elem.send_keys(Keys.DELETE)
    elem.send_keys(text)

    while elem == elem_before:
        time.sleep(1)
        continue

    if elem.get_attribute("id") == "PurchaseOrder_editView_fieldName_purchaseorder_no":
        assert (elem.get_attribute('value') == "P" + text)
    elif elem.get_attribute("id") == "Invoice_editView_fieldName_invoice_no":
        assert (elem.get_attribute('value') == "INV" + text)
    elif elem.get_attribute("id") == "Products_editView_fieldName_productname":
        assert (elem.get_attribute('value') == "_" + text)
    elif elem.get_attribute("id") == "Contacts_editView_fieldName_contact_no":
        assert (elem.get_attribute('value') == "CON" + text)
    else:
        assert (elem.get_attribute('value') == text) or (elem.get_attribute('value') == text.upper())


def fill_pn_fields(driver, value, text):
    if value != "pl_ins_but":
        try:
            elem = driver.find_elements(By.ID, value)[2]
            assert NoSuchElementException
        except:
            elem = driver.find_elements(By.XPATH, value)[2]
            assert NoSuchElementException

        elem.click()
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)
        elem.send_keys(text)
        assert (elem.get_attribute('value') == text)
    else:
        elem = driver.find_elements(By.ID, value)[2]
        assert NoSuchElementException
        elem.click()


def fill_new_pn_fields(driver, value, pn_text_field, addpn, text):
    if value != "pl_ins_but":
        try:
            elem = driver.find_element(By.ID, value)
            assert NoSuchElementException
        except:
            elem = driver.find_element(By.XPATH, value)
            assert NoSuchElementException

        elem.click()
        wait_element(driver, pn_text_field, 'id')
        elem = driver.find_element(By.ID, pn_text_field)
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)
        elem.send_keys(text)
        assert (elem.get_attribute('value') == text)
        driver.find_element(By.ID, addpn).click()
        driver.find_element(By.ID, addpn).click()
    else:
        elem = driver.find_elementt(By.ID, value)
        assert NoSuchElementException
        elem.click()


def wait_element(driver, value, type):
    elem = None
    time.sleep(0.5)
    while not elem:
        if type == 'xpath':
            try:
                elem = driver.find_element(By.XPATH, value)
            except NoSuchElementException:
                time.sleep(1)
        elif type == 'id':
            try:
                elem = driver.find_element(By.ID, value)
            except NoSuchElementException:
                time.sleep(1)
    return elem


def wait_element_by(driver, value, type):
    wait = WebDriverWait(driver, 10)
    time.sleep(0.2)

    if type == 'xpath':
        return driver.wait.until(EC.presence_of_element_located(By.XPATH, value))
    else:
        return driver.wait.until(EC.presence_of_element_located(By.ID, value))


def select_value_from_dropdown(driver, value, text):

    driver.find_element(By.ID, value).click()
    i = 0
    if driver.find_elements(By.XPATH, text)[i].text is not '':
        driver.find_elements(By.XPATH, text)[i].click()
    else:
        i += 1
    #assert str(driver.find_element(By.ID, value).text).split("\n")[0] == text.split('\"')[1]


def change_sales_type(driver, value, text):

    try:
        Select(driver.find_element_by_id(value)).select_by_visible_text(text)  # do something
    except socket.error as e:
        Select(driver.find_element_by_id(value)).select_by_visible_text(text)  # A socket error
    except IOError as e:
        Select(driver.find_element_by_id(value)).select_by_visible_text(text)
        if e.errno == errno.EPIPE:
            Select(driver.find_element_by_id(value)).select_by_visible_text(text)  # EPIPE error
        else:
            Select(driver.find_element_by_id(value)).select_by_visible_text(text)  # Other error


def wait_product_field_selection(driver):
    i = 0
    while i < 10:
        try:
            driver.find_element(By.ID, "productName1").get_attribute("disabled") == 'true'
            time.sleep(0.5)
            i = 10
        except:
            time.sleep(0.5)
            i += 1


def select_calendar_date(driver, field, value):
    elem = driver.find_element(By.ID, field)
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(value)
    assert elem.get_attribute("value") == value


def select_table_cell(driver, field, tab, url):
    data_id = driver.find_element(By.ID, field).get_attribute("data-id")
    table = driver.find_element(By.ID, field)
    value = table.find_elements_by_tag_name('a')[0].text
    value = '//tr//td[contains(.,"' + value + '")]'
    table.find_element(By.XPATH, value).click()
    if tab == "so":
        assert url + "index.php?module=SalesOrder&view=Detail&record=" + data_id == driver.current_url
    elif tab == "po":
        assert url + "index.php?module=PurchaseOrder&view=Detail&record=" + data_id == driver.current_url


# def get_so_number(driver, value):
#     so_num = driver.find_element(By.ID, "SalesOrder_listView_row_1").text.split(' ')[0]
#     return so_num


# def change_data_file(value):
#     if value == "rfq":
#         data = rfq_data
#     elif value == "quote":
#         data = quotes_data
#     elif value == "so":
#         data = so_data
#     elif value == "auth":
#         data = authorization_data
#     else:
#         data = po_data
#     return data


def overwrite_elements(driver, value, button):
    elements = driver.find_elements(By.XPATH, value)
    elements_qty = len(driver.find_elements(By.XPATH, value))
    i = 0
    while i < elements_qty:
        elements[i].click()
        i += 1
    driver.find_element(By.XPATH, button).click()


def wait_element_vanishing(driver, value):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located((By.ID, value)))


def wait_element_for_click(driver, value):
    i = 0
    while i < 10:
        try:
            click_element_by_id(driver, value).click()
            i = 10
        except:
            time.sleep(1)
            i += 1


def select_element_with_text_from_list(driver, value, type, text):
    i = 0
    if type == 'id':
        wait_element(driver, value, 'id')
        qtyelements = len(driver.find_elements(By.ID, value))
        identificator = By.ID
    elif type == 'xpath':
        wait_element(driver, value, 'xpath')
        qtyelements = len(driver.find_elements(By.XPATH, value))
        identificator = By.XPATH

    while i < qtyelements:
        if driver.find_elements(identificator, value)[i].text == text and (
                driver.find_elements(identificator, value)[i].text.find('\n') == -1) is True:
            driver.find_elements(identificator, value)[i].click()
            i = qtyelements
        else:
            i = i + 1


def select_category_all(driver):
    wait_element(driver, data.all_categories_id, 'id')
    try:
        driver.find_element(By.ID, data.all_categories_id).click()
        assert bool(driver.find_element(By.XPATH, '//li[@class="dropdown open" and @id="moreMenu"]')) is True
    except:
        time.sleep(1)
        driver.find_element(By.ID, data.all_categories_id).click()
        assert bool(driver.find_element(By.XPATH, '//li[@class="dropdown open" and @id="moreMenu"]')) is True


def check_all_item_checkbuttons(driver):
    i = 0
    while i < len(driver.find_elements(By.XPATH, '//input[@type="checkbox"]')):
        if driver.find_elements(By.XPATH, '//input[@type="checkbox"]')[i].size == {'height': 20.0, 'width': 20.0}:
            driver.find_elements(By.XPATH, '//input[@type="checkbox"]')[i].click()
            i = len(driver.find_elements(By.XPATH, '//input[@type="checkbox"]'))
        else:
            i += 1


def wait_new_page(driver, new_url):
    i = 0
    while driver.current_url == new_url:
        if i < 40:
            time.sleep(0.2)
            i += 1
            continue
        else:
            break
        time.sleep(2)


def select_last_element_from_list(driver, value):
    Select(driver.find_element_by_id(value)).select_by_visible_text(
        driver.find_element(By.ID, value).text.split("\n")[
            len(driver.find_element(By.ID, value).text.split("\n")) - 1])


def check_all_item_checkbuttonspo(driver, value):
    i = 0
    while i < len(driver.find_elements(By.XPATH, value)):
        if driver.find_elements(By.XPATH, value)[i].size == {'height': 24.0, 'width': 24.0}:
            driver.find_elements(By.XPATH, value)[i].click()
            i += 1
        else:
            i += 1


def select_last_material_arrival_inspection(driver, value, page):
    wait_element(driver, value, 'id')
    driver.find_element(By.ID, value).click()
    time.sleep(10)
    if page == "inspection":
        driver.find_elements(By.XPATH, '//input[@class="chzn-search-input" and @type="text"]')[1].click()
        driver.find_elements(By.XPATH, '//input[@class="chzn-search-input" and @type="text"]')[1].send_keys("getmansky")
    else:
        driver.find_elements(By.XPATH, '//input[@class="chzn-search-input" and @type="text"]')[1].click()
    driver.find_elements(By.XPATH, '//li[@class="active-result"]')[len(driver.find_elements(By.XPATH, '//li[@class="active-result"]')) - 1].click()


def click_material_arrival_buttons(driver, value):
    #value = data.deliver_button
    driver.find_elements(By.XPATH, value)[
        len(driver.find_elements(By.XPATH, value)) - 1].click()

