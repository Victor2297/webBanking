import time

from pytest_bdd import given, when, then, scenario

from utilities.logs import GetLogs

logger = GetLogs.get_logs('new_customer')

#Background
@given('user goes on the login page')
def user_goes_on_the_login_page(get_driver, get_ReadProperties_class):
    get_driver.get(get_ReadProperties_class.get_login_page_url())
    logger.debug('The login page is opened')

@given('logins on the page')
def logins_on_the_page(get_LoginPage_class):
    get_LoginPage_class.fill_username('mngr435545')
    get_LoginPage_class.fill_password('ugadAse')
    logger.debug('The username field and password field is filled')
    get_LoginPage_class.click_login()
    logger.debug('Clicked on the login button')


#Create_new_customer
@scenario('../features/new_customer.feature', 'Create_new_customer')
def test_new_customer():
    pass

@given('user clicks on the new customer button')
def user_clicks_on_the_new_customer_button(get_NewCustomer_class):
    new_customer = get_NewCustomer_class

    new_customer.click_on_the_new_customer_button()
    logger.debug('Clicked on the new customer  button')
    new_customer.close_ad()

@when('fills all fields from opened page')
def fills_all_fields_from_opened_page(get_NewCustomer_class):
    new_customer = get_NewCustomer_class

    new_customer.fill_customer_name('Victor')
    new_customer.fill_customer_dob('11111990')
    new_customer.fill_customer_address('Street1')
    new_customer.fill_customer_city('NYC')
    new_customer.fill_customer_state('NYC')
    new_customer.fill_customer_pin('123456')
    new_customer.fill_customer_telephone('3456678457456')
    new_customer.fill_customer_email(new_customer.get_random_email(10))
    new_customer.fill_customer_password('2345675678')
    logger.debug('All fields from new customer page are filled')

@when('clicks on the submit button')
def clicks_on_the_submit_button(get_NewCustomer_class):
    new_customer = get_NewCustomer_class

    new_customer.click_submit_button()
    logger.debug('The data is submitted')

@then('user sees Registered Successfully message')
def user_sees_Registered_Successfully_message(get_NewCustomer_class):
    time.sleep(3)
    if get_NewCustomer_class.is_alert_present() == True:
        assert False, 'Alert is present'
        logger.debug('Test Failed')
    else:
        if 'Customer Registered Successfully!!!' in get_NewCustomer_class.driver.page_source:
            assert True
            logger.debug('Test Passed')
        else:
            assert False, 'Customer Registered Successfully message is missing!!!'
            logger.debug('Test Failed')
