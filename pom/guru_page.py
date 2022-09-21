from base.base_class import BaseClass
from utilities.read_properties import ReadProperties


class GuruPage(BaseClass):
    guru_logo_xpath = ReadProperties.get_guru_logo()
    guru_hello_message_xpath = ReadProperties.get_guru_hello_message()

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_guru_logo_element(self):
        return self.is_clickable('xpath', GuruPage.guru_logo_xpath)

    def click_on_logo_element(self):
        self.get_guru_logo_element().click()

    def get_guru_page_url(self):
        return self.driver.current_url

    def get_guru_hello_message_text(self):
        return self.is_present('xpath', GuruPage.guru_hello_message_xpath).text