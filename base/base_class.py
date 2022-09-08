import random
import string

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utilities.read_properties import ReadProperties


class BaseClass:
    ad_parent_frame_id = ReadProperties.get_ad_parent_frame()
    ad_child_frame_id = ReadProperties.get_ad_child_frame()
    ad_dismiss_button_id = ReadProperties.get_ad_dismiss_button()

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

    def is_frame_present(self, frame_locator):
        try:
            self.driver.switch_to.frame(frame_locator)
            print('Ad was displayed')
            return True
        except:
            print('Ad was not displayed')
            return False

    def get_random_email(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str + '@gmail.com'

    def click_on_the_close_ad_button(self):
        self.is_clickable('id', BaseClass.ad_dismiss_button_id).click()

    def close_ad(self):
        if self.is_frame_present(BaseClass.ad_parent_frame_id) == True:
            try:
                self.click_on_the_close_ad_button()
            except:
                self.driver.switch_to.frame(BaseClass.ad_child_frame_id())
                self.click_on_the_close_ad_button()
            print('Ads was displayed')
        else:
            print('Ads was not displayed')