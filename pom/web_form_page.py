"""Web form page"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.web_form_page_target import WebFormTargetPage


class WebFormPage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.title = "Web form"

    _my_textarea = By.NAME, "my-textarea"
    _submit_form = By.CSS_SELECTOR, ".btn"

    def set_textarea(self, text: str):
        self.driver.find_element(*self._my_textarea).send_keys(text)
        return self

    def submit_form(self):
        self.driver.find_element(*self._submit_form).click()
        return WebFormTargetPage(self.driver)
