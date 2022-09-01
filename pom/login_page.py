from selenium.webdriver.common.by import By

from base.base_class import BaseClass
from utilities.read_properties import ReadProperties


class LoginPage(BaseClass):
    username_input_name = ReadProperties.get_username_input()
    password_input_name = ReadProperties.get_password_input()
    login_button_name = ReadProperties.get_login_button()
    manager_id_xpath = ReadProperties.get_manager_id()

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def get_username(self):
        return self.is_present('name', LoginPage.username_input_name)

    def get_password(self):
        return self.is_present('name', LoginPage.password_input_name)

    def get_login_button(self):
        return self.is_clickable('name', LoginPage.login_button_name)

    def fill_username(self, uname):
        self.get_username().send_keys(uname)

    def fill_password(self, upass):
        self.get_password().send_keys(upass)

    def click_login(self):
        self.get_login_button().click()

    def get_manager_id_text(self):
        return self.is_present('xpath', LoginPage.manager_id_xpath).text