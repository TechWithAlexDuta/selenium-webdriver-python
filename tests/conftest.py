"""Test fixture"""

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    # Setup: Create a browser instance
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.maximize_window()

    # Provide the fixture value
    yield driver

    # Teardown: Quit the browser instance
    driver.quit()
