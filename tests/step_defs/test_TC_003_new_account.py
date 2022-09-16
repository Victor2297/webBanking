from pytest_bdd import given, when, then, scenario

from utilities.logs import GetLogs

logger = GetLogs.get_logs('new_account')

#create new account
@scenario('new_account.feature', 'Create new account')
def test_new_account():
    pass

@given('user clicks on the new account button')
def user_clicks_on_the_new_account_button(get_NewAccount_class):
    get_NewAccount_class.click_new_account_button()
    logger.debug('The new account page is opened')
    get_NewAccount_class.close_ad()

@when('user fills all fields')
def user_fills_all_fields(get_NewAccount_class):
    get_NewAccount_class.fill_customer_id('57802')
    get_NewAccount_class.fill_initial_deposit('123422')
    logger.debug('All fields from New Account page are filled')

@when('clicks on the submit button')
def clicks_on_the_submit_button(get_NewAccount_class):
    get_NewAccount_class.click_submit_button()
    logger.debug('The data are submitted')

@then('user sees account id and the same amount')
def user_sees_account_id_and_the_same_amount(get_NewAccount_class):
    if len(get_NewAccount_class.get_account_id()) and len(get_NewAccount_class.get_current_amount()) > 5:
        assert True
        logger.debug('Test Passed')
    else:
        assert False, logger.debug('Test Failed, the data are invalid')