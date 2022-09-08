from base.base_class import BaseClass
from utilities.read_properties import ReadProperties


class NewCustomer(BaseClass):
    new_customer_button_xpath = ReadProperties.get_new_customer_button()
    c_name_name = ReadProperties.get_c_name()
    c_dob_name = ReadProperties.get_c_dob()
    c_address_name = ReadProperties.get_c_address()
    c_city_name = ReadProperties.get_c_city()
    c_state_name = ReadProperties.get_c_state()
    c_pin_name = ReadProperties.get_c_pin()
    c_telephoneno_name = ReadProperties.get_c_telephoneno()
    c_email_name = ReadProperties.get_c_email()
    c_password_name = ReadProperties.get_password_input()
    submit_button_name = ReadProperties.get_submit_button()

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_on_the_new_customer_button(self):
        self.is_clickable('xpath', NewCustomer.new_customer_button_xpath).click()

    def fill_customer_name(self, c_name):
        self.is_present('name', NewCustomer.c_name_name).send_keys(c_name)

    def fill_customer_dob(self, c_dob):
        self.is_present('name', NewCustomer.c_dob_name).send_keys(c_dob)

    def fill_customer_address(self, c_address):
        self.is_present('name', NewCustomer.c_address_name).send_keys(c_address)

    def fill_customer_city(self, c_city):
        self.is_present('name', NewCustomer.c_city_name).send_keys(c_city)

    def fill_customer_state(self, c_state):
        self.is_present('name', NewCustomer.c_state_name).send_keys(c_state)

    def fill_customer_pin(self, c_pin):
        self.is_present('name', NewCustomer.c_pin_name).send_keys(c_pin)

    def fill_customer_telephone(self, c_telephone):
        self.is_present('name', NewCustomer.c_telephoneno_name).send_keys(c_telephone)

    def fill_customer_email(self, c_email):
        self.is_present('name', NewCustomer.c_email_name).send_keys(c_email)

    def fill_customer_password(self, c_password):
        self.is_present('name', NewCustomer.c_password_name).send_keys(c_password)

    def click_submit_button(self):
        self.is_clickable('name', NewCustomer.submit_button_name).click()
