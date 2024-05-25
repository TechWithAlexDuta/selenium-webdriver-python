"""Web form - parget page"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGGER = logging.getLogger(__name__)


class WebFormTargetPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.title = "Web form - target page"

    _message = By.ID, "message"

    def get_message(self):
        actual_message = self.driver.find_element(*self._message).text
        LOGGER.info(f"actual message is:[{actual_message}]")
        return actual_message
