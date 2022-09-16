from base.base_class import BaseClass
from utilities.read_properties import ReadProperties


class NewAccount(BaseClass):
    new_account_button_xpath = ReadProperties.get_new_account_button()
    customer_id_input_name = ReadProperties.get_customer_id_input()
    initial_deposit_input_name = ReadProperties.get_initial_deposit_input()
    submit_button_name = ReadProperties.get_submit_button2()
    account_id_field_xpath = ReadProperties.get_account_id_field()
    current_amount_field_xpath = ReadProperties.get_current_amount_field()

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_new_account_button(self):
        self.is_clickable('xpath', NewAccount.new_account_button_xpath).click()

    def get_customer_id_element(self):
        return self.is_present('name', NewAccount.customer_id_input_name)

    def fill_customer_id(self, customer_id):
        self.get_customer_id_element().send_keys(customer_id)

    def get_initial_deposit_element(self):
        return self.is_present('name', NewAccount.initial_deposit_input_name)

    def fill_initial_deposit(self, initial_deposit):
        self.get_initial_deposit_element().send_keys(initial_deposit)

    def click_submit_button(self):
        self.is_clickable('name', NewAccount.submit_button_name).click()

    def get_account_id(self):
        return self.is_present('xpath', NewAccount.account_id_field_xpath).text

    def get_current_amount(self):
        return self.is_present('xpath', NewAccount.current_amount_field_xpath).text