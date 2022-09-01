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