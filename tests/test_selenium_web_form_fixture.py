"""Sample test with conftest and pytest fixture"""

import uuid
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_write_to_text_area_and_submit_fixture(browser):
    expected_message = "Received!"
    text = str(uuid.uuid4())

    browser.find_element(By.NAME, "my-textarea").send_keys(text)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    message = browser.find_element(By.ID, "message").text

    assert message == expected_message


if __name__ == "__main__":
    pytest.main()
