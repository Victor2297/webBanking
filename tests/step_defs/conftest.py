import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_ch
from selenium.webdriver.chrome.service import Service as Service_ch
from selenium.webdriver.firefox.service import Service as Service_ff
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pom.guru_page import GuruPage
from pom.login_page import LoginPage
from pom.new_account import NewAccount
from pom.new_customer import NewCustomer
from utilities.read_properties import ReadProperties


# @pytest.fixture
# def get_options():
#     options = Options_ch()
#     options.add_argument('start-maximized')
#     options.add_experimental_option('detach', True)
#     return options
#
# @pytest.fixture
# def get_webdriver_chrome(get_options):
#     options = get_options
#     service = Service_ch(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     return driver
#
# @pytest.fixture
# def get_webdriver_firefox():
#     service = Service_ff(executable_path=GeckoDriverManager().install())
#     driver = webdriver.Firefox(service=service)
#     return driver
#
# @pytest.fixture
# def setup(get_webdriver_chrome):
#     driver = get_webdriver_chrome
#     return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="session")
def get_browser(pytestconfig):
    return pytestconfig.getoption("browser")

@pytest.fixture
def setup(get_browser):
    if get_browser == 'chrome':
        options = Options_ch()
        options.add_argument('start-maximized')
        options.add_experimental_option('detach', True)
        service = Service_ch(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    if get_browser == 'firefox':
        service = Service_ff(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        return driver
    return get_browser


##########################################
@pytest.fixture
def get_driver(setup):
    driver = setup
    return driver

@pytest.fixture
def get_ReadProperties_class():
    return ReadProperties

@pytest.fixture
def get_LoginPage_class(get_driver):
    return LoginPage(get_driver)

@pytest.fixture
def get_NewCustomer_class(get_driver):
    return NewCustomer(get_driver)

@pytest.fixture
def get_NewAccount_class(get_driver):
    return NewAccount(get_driver)

@pytest.fixture
def get_GuruPage_class(get_driver):
    return GuruPage(get_driver)

def pytest_bdd_before_scenario(request, feature, scenario):
    driver = request.getfixturevalue('get_driver')
    read_properties = request.getfixturevalue('get_ReadProperties_class')
    login_page = request.getfixturevalue('get_LoginPage_class')
    #user goes to login page
    driver.get(read_properties.get_login_page_url())
    #logins on the page
    login_page.fill_username('mngr443133')
    login_page.fill_password('seqeqYq')
    login_page.click_login()