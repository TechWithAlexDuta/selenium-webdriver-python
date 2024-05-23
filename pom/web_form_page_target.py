"""Web form - parget page"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class WebFormTargetPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.title = "Web form - target page"

    _message = By.ID, "message"

    def get_message(self):
        return self.driver.find_element(*self._message).text
