import time

from pytest_bdd import scenario, given, when, then, parsers


#background
@given('user goes on the login page')
def user_goes_on_the_login_page(get_driver, get_ReadProperties_class):
    get_driver.get(get_ReadProperties_class.get_login_page_url())

#scenario Login_with_valid_data
@scenario('../features\login.feature', 'Login_with_valid_data')
def test_login_valid_data():
    pass

@given(parsers.parse('user fills username "{username}" field'))
def user_fills_username_field(get_LoginPage_class, username):
    get_LoginPage_class.fill_username(username)

@given(parsers.parse('user fills password "{password}" field'))
def user_fills_password_field(get_LoginPage_class, password):
    get_LoginPage_class.fill_password(password)

@when('user clicks on the login button')
def user_clicks_on_the_login_button(get_LoginPage_class):
    get_LoginPage_class.click_login()
    time.sleep(3)

@then(parsers.parse('user sees the username "{username}" on the hello page'))
def user_sees_the_username_on_the_hello_page(get_LoginPage_class, username):
    if get_LoginPage_class.is_alert_present() == True:
        print('Test Failed')
        assert False
    else:
        assert username in get_LoginPage_class.get_manager_id_text()

@scenario('../features/login.feature', 'Login_with_invalid_data')
def test_login_invalid_data():
    pass

#scenario Login_with_invalid_data
@given(parsers.parse('user fills username {u} field'))
def user_fills_username_field(u, get_LoginPage_class):
    get_LoginPage_class.fill_username(u)

@given(parsers.parse('user fills password {p} field'))
def user_fills_password_password_field(p, get_LoginPage_class):
    get_LoginPage_class.fill_password(p)

@then('user sees the alert pop up')
def user_sees_the_alert_pop_up(get_driver, get_LoginPage_class):
    if get_LoginPage_class.is_alert_present() == True:
        get_driver.switch_to.alert.accept()
        get_driver.switch_to.default_content()
        assert True
    else:
        assert False