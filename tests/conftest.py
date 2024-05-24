"""Test fixture"""

import pytest
from selenium import webdriver

from config.browser_type import Browser
from config.web_settings import BASE_URL
from config.web_settings import BROWSER
from config.web_settings import IMPLICIT_WAIT


@pytest.fixture
def browser():
    # Setup: Create a browser instance
    match BROWSER:
        case Browser.CHROME:
            driver = webdriver.Chrome()
        case Browser.FIREFOX:
            driver = webdriver.Firefox()
        case Browser.EDGE:
            driver = webdriver.Edge()
        case _:
            raise ValueError(f"Browser not supported {BROWSER}")
        
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait = IMPLICIT_WAIT

    # Provide the fixture value
    yield driver

    # Teardown: Quit the browser instance
    driver.quit()
