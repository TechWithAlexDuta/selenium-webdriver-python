"""Web form page"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.web_form_page_target import WebFormTargetPage

LOGGER = logging.getLogger(__name__)


class WebFormPage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.title = "Web form"

    _my_textarea = By.NAME, "my-textarea"
    _submit_form = By.CSS_SELECTOR, ".btn"

    def set_textarea(self, text: str):
        LOGGER.info(f"set text:[{text}] to element:[{self._my_textarea}]")
        self.driver.find_element(*self._my_textarea).send_keys(text)
        return self

    def submit_form(self):
        LOGGER.info(f"submit form - click on element:[{self._submit_form}]")
        self.driver.find_element(*self._submit_form).click()
        return WebFormTargetPage(self.driver)
