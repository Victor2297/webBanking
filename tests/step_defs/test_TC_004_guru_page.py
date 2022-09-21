from pytest_bdd import given, when, then, scenario, parsers

from utilities.logs import GetLogs

logger = GetLogs.get_logs('guru_page')

@scenario('guru_page.feature', 'Verify hello message and url')
def test_guru_page():
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