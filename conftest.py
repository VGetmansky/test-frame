import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="firefox", help="Type in browser type")
    parser.addoption("--url", action="store", default="http://crmtst_us.bai-inc.eu/", help="url") # http://wwwtst_us.bai-inc.eu/
    parser.addoption("--username", action="store", default="vladislav.getmanskiy@zimad.com", help="username")
    parser.addoption("--password", action="store", default="Welcome2018!", help="password")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'firefox':

        firefoxoptions = webdriver.FirefoxProfile()
        firefoxoptions.set_preference("security.insecure_password.ui.enabled", False)
        firefoxoptions.set_preference("security.insecure_field_warning.contextual.enabled", False);
        browser = webdriver.Firefox(firefoxoptions)
        browser.get("about:blank")
        browser.implicitly_wait(10)
        browser.maximize_window()

        return browser

    else:
        print('only firefox is supported at the moment')


@pytest.fixture(scope="module")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")

# @pytest.fixture(scope="module")
# def pytest_runtest_teardown(request):
#     request.browser.teardown()
