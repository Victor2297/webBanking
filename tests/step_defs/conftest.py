import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_ch
from selenium.webdriver.chrome.service import Service as Service_ch
from selenium.webdriver.firefox.service import Service as Service_ff
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pom.login_page import LoginPage
from utilities.read_properties import ReadProperties


@pytest.fixture
def get_options():
    options = Options_ch()
    options.add_argument('start-maximized')
    options.add_experimental_option('detach', True)
    return options

@pytest.fixture
def get_webdriver_chrome(get_options):
    options = get_options
    service = Service_ch(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@pytest.fixture
def get_webdriver_firefox():
    service = Service_ff(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    return driver

@pytest.fixture
def setup(get_webdriver_chrome):
    driver = get_webdriver_chrome
    return driver

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