from selenium.webdriver.common.by import By

from base.base_class import BaseClass
from utilities.read_properties import ReadProperties


class GuruPage(BaseClass):
    guru_logo_xpath = ReadProperties.get_guru_logo()
    guru_hello_message_xpath = ReadProperties.get_guru_hello_message()
    search_field_name = ReadProperties.get_search_field()
    search_button_xpath = ReadProperties.get_search_button()
    result_window_xpath = ReadProperties.get_result_window()
    results_xpath = ReadProperties.get_results()

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

    def get_search_field(self):
        return self.is_present('name', GuruPage.search_field_name)

    def fill_guru_search_field(self, search_text):
        self.get_search_field().send_keys(search_text)

    def get_search_button(self):
        return self.is_clickable('xpath', GuruPage.search_button_xpath)

    def click_guru_search_button(self):
        self.get_search_button().click()

    def wait_until_the_result_window_is_present(self):
        self.is_present('xpath', GuruPage.result_window_xpath)

    def get_list_of_results(self):
        results = self.driver.find_elements(By.XPATH, GuruPage.results_xpath)
        list_results_text = []
        for result in results:
            list_results_text.append(result.text)
        return list_results_text
