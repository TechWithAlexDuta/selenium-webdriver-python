"""Test fixture"""

import logging
import pytest
from selenium import webdriver

from config.browser_type import Browser
from config.web_settings import BASE_URL
from config.web_settings import BROWSER
from config.web_settings import IMPLICIT_WAIT

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def browser():
    # Setup: Create a browser instance
    LOGGER.info("starting test")
    LOGGER.info(f"browser used: {BROWSER}")

    match BROWSER:
        case Browser.CHROME:
            driver = webdriver.Chrome()
        case Browser.FIREFOX:
            driver = webdriver.Firefox()
        case Browser.EDGE:
            driver = webdriver.Edge()
        case _:
            raise ValueError(f"Browser not supported {BROWSER}")

    LOGGER.info(f"base url: {BASE_URL}")
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait = IMPLICIT_WAIT

    # Provide the fixture value
    yield driver

    # Teardown: Quit the browser instance
    LOGGER.info("ending test")
    driver.quit()
