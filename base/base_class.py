from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_locators(self, find_by):
        locators = {
            'css': By.CSS_SELECTOR,
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
        }
        return locators[find_by]

    def is_present(self, find_by: str, locator: str) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.get_locators(find_by), locator)))

    def is_clickable(self, find_by: str, locator: str) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable((self.get_locators(find_by), locator)))

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False
