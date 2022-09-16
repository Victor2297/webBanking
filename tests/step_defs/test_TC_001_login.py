import time

from pytest_bdd import scenario, given, when, then, parsers

from utilities.logs import GetLogs

logger = GetLogs.get_logs('login')

#background
@given('user goes on the login page')
def user_goes_on_the_login_page(get_driver, get_ReadProperties_class):
    get_driver.get(get_ReadProperties_class.get_login_page_url())
    logger.debug('The login page is opened')

#scenario Login_with_valid_data
@scenario('login.feature', 'Login_with_valid_data')
def test_login_valid_data():
    pass

@given(parsers.parse('user fills username "{username}" field'))
def user_fills_username_field(get_LoginPage_class, username):
    get_LoginPage_class.fill_username(username)
    logger.debug('The username field is filled')

@given(parsers.parse('user fills password "{password}" field'))
def user_fills_password_field(get_LoginPage_class, password):
    get_LoginPage_class.fill_password(password)
    logger.debug('The password field is filled')

@when('user clicks on the login button')
def user_clicks_on_the_login_button(get_LoginPage_class):
    get_LoginPage_class.click_login()
    logger.debug('Clicked on the login page')
    time.sleep(5)

@then(parsers.parse('user sees the username "{username}" on the hello page'))
def user_sees_the_username_on_the_hello_page(get_LoginPage_class, username):
    if get_LoginPage_class.is_alert_present() == True:
        print('Test Failed')
        logger.debug('Test Failed, the alert is present')
        assert False
    else:
        assert username in get_LoginPage_class.get_manager_id_text(), logger.debug('Test Failed, the user does not see the username')
        logger.debug('Test Passed, the user sees the username')
        logger.debug('')

@scenario('login.feature', 'Login_with_invalid_data')
def test_login_invalid_data():
    pass

#scenario Login_with_invalid_data
@given(parsers.parse('user fills username {u} field'))
def user_fills_username_field(u, get_LoginPage_class):
    get_LoginPage_class.fill_username(u)
    logger.debug('The username field is filled')

@given(parsers.parse('user fills password {p} field'))
def user_fills_password_password_field(p, get_LoginPage_class):
    get_LoginPage_class.fill_password(p)
    logger.debug('The password field is filled')

@then('user sees the alert pop up')
def user_sees_the_alert_pop_up(get_driver, get_LoginPage_class):
    if get_LoginPage_class.is_alert_present() == True:
        get_driver.switch_to.alert.accept()
        get_driver.switch_to.default_content()
        assert True
        logger.debug('Test Passed, the user can not login with wrong username and password')
        logger.debug('')
    else:
        assert False, logger.debug('Test Failed, the user can login with wrong username and password')