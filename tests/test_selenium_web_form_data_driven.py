"""Sample data driven test"""

import logging
import pytest

from pom.web_form_page import WebFormPage
from utils.reader import get_csv_data

LOGGER = logging.getLogger(__name__)

# run test and generate html report: pytest -m selenium_data_driven --html=results.html

@pytest.mark.selenium_data_driven
@pytest.mark.parametrize("test_data", get_csv_data('data\csv\data_driven.csv'))
def test_data_driven(test_data, browser):

    LOGGER.info(f'test case id:[{test_data['test_case_id']}] write text to textarea and submit form')

    web_form = WebFormPage(browser)
    message = web_form\
        .set_textarea(test_data['text_to_use'])\
        .submit_form()\
        .get_message()

    LOGGER.info(f'check that actual message:[{message}] == [{test_data['expected_message']}]')
    assert message == test_data['expected_message']


if __name__ == "__main__":
    pytest.main()
