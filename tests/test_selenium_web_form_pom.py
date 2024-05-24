"""Sample test with Page Object Model pattern"""

import pytest

from data.text_data import RECEIVED_EXPECTED_MESSAGE
from data.text_data import UUID
from pom.web_form_page import WebFormPage

@pytest.mark.selenium_pom
def test_write_to_text_area_and_submit_fixture(browser):

    web_form = WebFormPage(browser)
    message = web_form\
        .set_textarea(UUID)\
        .submit_form()\
        .get_message()

    assert message == RECEIVED_EXPECTED_MESSAGE


if __name__ == "__main__":
    pytest.main()
