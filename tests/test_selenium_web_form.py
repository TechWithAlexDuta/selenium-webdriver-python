"""Basic sample test """

import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_write_to_text_area_and_submit():
    expected_message = "Received!"
    text = str(uuid.uuid4())

    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.maximize_window()

    driver.find_element(By.NAME, "my-textarea").send_keys(text)
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    message = driver.find_element(By.ID, "message").text

    assert message == expected_message

    driver.quit()
