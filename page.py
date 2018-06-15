import functools
from lib2to3.pgen2 import driver
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def resend_request(func, count=5):
    for i in range(count):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)
        return wrapper


def check(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except TimeoutException:
            raise TimeoutException('TimeoutException: element with %s not found' % str(*args))
        except NoSuchElementException:
            raise NoSuchElementException('NoSuchElementException: element with %s not found' % str(*args))
        except ConnectionRefusedError:
            resend_request(func)
    return wrapper


def boolean(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
            return True
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
    return wrapper


def wait_new_page(func, *args, **kwargs):
    def wrapped(self, *args, **kwargs):
        from page import Page
        driver = Page().driver
        old_url = driver.current_url
        res = func(self, *args, **kwargs)
        for i in range(120):
            if old_url != driver.current_url:
                print('new page detected')
                break
            print('waiting new page..')
            sleep(0.5)
        else:
            return False
        return res

    return wrapped


class Page:
    def __init__(self):
        super(Page, self).__init__()
        self.driver = driver.Driver.instance
        self.wait = WebDriverWait(self.driver, 30)
        self.long_wait = WebDriverWait(self.driver, 90)

    @check
    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located((locator[0], locator[1])))

    @check
    def wait_presence_by_xpath(self, xpath, long=False):
        if long:
            return self.long_wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    @check
    def wait_presence_by_css(self, css_selector, long=False):
        if long:
            return self.long_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    @check
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable((locator[0], locator[1])))

    def wait_clickable_by_xpath(self, xpath, long=False):
        if long:
            return self.long_wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def wait_clickable_by_css(self, css_selector, long=False):
        if long:
            return self.long_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    @check
    def wait_all_presence_by_xpath(self, xpath, long=False):
        if long:
            return self.long_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    @check
    def wait_all_presence_by_css(self, css, long=False):
        if long:
            return self.long_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
        return self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))

    @check
    def wait_until_hidden(self, locator):
        try:
            self.wait.until_not(EC.visibility_of_element_located((locator[0], locator[1])))
            return True
        except TimeoutException:
            return False

    @check
    def wait_until_hidden2(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((locator[0], locator[1])))
            return True
        except TimeoutException:
            return False

    # +++ CSS


    # --- CSS


    @check
    def _find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def switch_to_frame(self, iframe_locator):
        try:
            assert self.wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_locator)), 'ERROR: switch_to_frame'
        except UnexpectedAlertPresentException as err:
            print('UnexpectedAlertPresentException CHECKED!')
            print(err.msg)
            self.driver.switch_to_alert().accept()
            return self.switch_to_frame(iframe_locator)

    def switch_to_default_content(self):
        assert self.wait.until(EC.frame_to_be_available_and_switch_to_it((None))), 'ERROR: switch_to_default_content'

    def switch_to_frame_and_back(self, iframe_locator, func, arg=None):
        self.switch_to_frame(iframe_locator)
        try:
            if arg:
                return func(arg)
            else:
                return func()
        except TimeoutException:
            print('%s not found' % func)
            return False
        finally:
            self.switch_to_default_content()

    def javascript_to_set_new_value_to_element(self, new_value, element):
        self.driver.execute_script('arguments[0].value = arguments[1]', element, new_value)

