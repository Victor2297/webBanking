import configparser

conf = configparser.ConfigParser()
conf.read('C:\\Users\\Victor\\PycharmProjects\\web_banking\\Configurations\\config.ini')

class ReadProperties:
    @staticmethod
    def get_username_input():
        return conf.get('LoginSection', 'username_input_name')

    @staticmethod
    def get_password_input():
        return conf.get('LoginSection', 'password_input_name')

    @staticmethod
    def get_login_button():
        return conf.get('LoginSection', 'login_button_name')

    @staticmethod
    def get_manager_id():
        return conf.get('LoginSection', 'manager_id_xpath')

    @staticmethod
    def get_login_page_url():
        return conf.get('LoginSection', 'login_page_url')

    @staticmethod
    def get_new_customer_button():
        return conf.get('NewCustomerSection', 'new_customer_button_xpath')

    @staticmethod
    def get_c_name():
        return conf.get('NewCustomerSection', 'c_name_name')

    @staticmethod
    def get_c_dob():
        return conf.get('NewCustomerSection', 'c_dob_name')

    @staticmethod
    def get_c_address():
        return conf.get('NewCustomerSection', 'c_address_name')

    @staticmethod
    def get_c_city():
        return conf.get('NewCustomerSection', 'c_city_name')

    @staticmethod
    def get_c_state():
        return conf.get('NewCustomerSection', 'c_state_name')

    @staticmethod
    def get_c_pin():
        return conf.get('NewCustomerSection', 'c_pin_name')

    @staticmethod
    def get_c_telephoneno():
        return conf.get('NewCustomerSection', 'c_telephoneno_name')

    @staticmethod
    def get_c_email():
        return conf.get('NewCustomerSection', 'c_email_name')

    @staticmethod
    def get_c_password():
        return conf.get('NewCustomerSection', 'c_password_name')

    @staticmethod
    def get_submit_button():
        return conf.get('NewCustomerSection', 'submit_button_name')

    @staticmethod
    def get_ad_parent_frame():
        return conf.get('AdsSection', 'ad_parent_frame_id')

    @staticmethod
    def get_ad_child_frame():
        return conf.get('AdsSection', 'ad_child_frame_id')

    @staticmethod
    def get_ad_dismiss_button():
        return conf.get('AdsSection', 'ad_dismiss_button_id')