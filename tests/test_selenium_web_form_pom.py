"""Sample test with Page Object Model pattern"""

import logging
import pytest

from data.text_data import RECEIVED_EXPECTED_MESSAGE
from data.text_data import UUID
from pom.web_form_page import WebFormPage

LOGGER = logging.getLogger(__name__)

# run test and generate html report: pytest -m selenium_pom --html=results.html
# run test and generate html report with self-contained-html: pytest -m selenium_pom --html=results.html --self-contained-html

@pytest.mark.selenium_pom
@pytest.mark.selenium
def test_write_to_text_area_and_submit_fixture(browser):

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
