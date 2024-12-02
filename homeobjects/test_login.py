import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        username_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
        )
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_field.send_keys(password)

    def clickLogin(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Login']"))
        )
        login_button.click()

    def actualError(self):
        try:
            error_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[text()='Wrong credentials']"))
            )
            return error_element.text
        except TimeoutException:
            return None


