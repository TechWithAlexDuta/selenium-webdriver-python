"""Sample tests to run in parallel"""

import logging
import pytest

from data.text_data import RECEIVED_EXPECTED_MESSAGE
from data.text_data import UUID
from pom.web_form_page import WebFormPage

LOGGER = logging.getLogger(__name__)

# run tests in parallel and generate html report: pytest -m selenium_parallel -n auto --html=report.html


@pytest.mark.selenium_parallel
def test_write_to_text_area_and_submit_parallel1(browser):

    LOGGER.info('write text to textarea and submit form')

    web_form = WebFormPage(browser)
    message = web_form\
        .set_textarea(UUID)\
        .submit_form()\
        .get_message()

    LOGGER.info(f'check that actual message:[{message}] == [{RECEIVED_EXPECTED_MESSAGE}]')
    assert message == RECEIVED_EXPECTED_MESSAGE

@pytest.mark.selenium_parallel
def test_write_to_text_area_and_submit_parallel2(browser):

    LOGGER.info('write text to textarea and submit form')

    web_form = WebFormPage(browser)
    message = web_form\
        .set_textarea(UUID)\
        .submit_form()\
        .get_message()

    LOGGER.info(f'check that actual message:[{message}] == [{RECEIVED_EXPECTED_MESSAGE}]')
    assert message == RECEIVED_EXPECTED_MESSAGE

@pytest.mark.selenium_parallel
def test_write_to_text_area_and_submit_parallel3(browser):

    LOGGER.info('write text to textarea and submit form')

    web_form = WebFormPage(browser)
    message = web_form\
        .set_textarea(UUID)\
        .submit_form()\
        .get_message()

    LOGGER.info(f'check that actual message:[{message}] == [{RECEIVED_EXPECTED_MESSAGE}]')
    assert message == RECEIVED_EXPECTED_MESSAGE

if __name__ == "__main__":
    pytest.main()
