import time

from pytest_bdd import given, when, then, scenario, parsers

from utilities.logs import GetLogs

logger = GetLogs.get_logs('guru_page')

@scenario('guru_page.feature', 'Verify hello message and url')
def test_guru_url_and_hello_message():
    pass

@given('click guru logo')
def click_guru_logo(get_GuruPage_class):
    get_GuruPage_class.click_on_logo_element()
    logger.debug('the logo is clicked')
    get_GuruPage_class.close_ad()

@then(parsers.parse('see hello message "{hello_message}" and the url "{url}"'))
def see_hello_message_and_the_url(get_GuruPage_class, hello_message, url):
    if str(get_GuruPage_class.get_guru_page_url()) == url:
        logger.debug('the url is right')
        if get_GuruPage_class.get_guru_hello_message_text() == hello_message:
            logger.debug('the hello message is the same')
            logger.debug('Test passed')
            assert True
        else:
            logger.debug('Test failed, the hello message differ')
            assert False

    else:
        logger.debug('Test failed, the data differ')
        assert False

@scenario('../features/guru_page.feature', 'Verify search from guru page')
def test_guru_search_and_results():
    pass

@given('click on guru logo')
def click_on_guru_logo(get_GuruPage_class):
    get_GuruPage_class.click_on_logo_element()
    logger.debug('The click is made on logo')

@when(parsers.parse('fill search field "{text_value}"'))
def fill_search_field(get_GuruPage_class, text_value):
    time.sleep(5)
    get_GuruPage_class.fill_guru_search_field(text_value)
    logger.debug('The search field is filled')

@when('click search button')
def click_search_button(get_GuruPage_class):
    get_GuruPage_class.click_guru_search_button()
    logger.debug('The search button is clicked')

@then(parsers.parse('results window contains the "{text_value}" text used in search'))
def results_window_contains_the_text_used_in_search(get_GuruPage_class, text_value):
    get_GuruPage_class.wait_until_the_result_window_is_present()
    for result in get_GuruPage_class.get_list_of_results():
        if result.startswith(text_value):
            assert True
        else:
            assert False, logger.debug('Test Failed')
    logger.debug('Test Passed')