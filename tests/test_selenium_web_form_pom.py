"""Sample test with Page Object Model pattern"""

import uuid
import pytest

from pom.web_form_page import WebFormPage

@pytest.mark.selenium_pom
def test_write_to_text_area_and_submit_fixture(browser):
    expected_message = "Received!"
    text = str(uuid.uuid4())

    web_form = WebFormPage(browser)
    message = web_form\
        .set_textarea(text)\
        .submit_form()\
        .get_message()

    assert message == expected_message
