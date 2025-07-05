from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def dologin(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.find(By.XPATH, "//span[text()='Dashboard']")
        sleep(3)
        print("\n\nLogin successful!")

    def enter_username(self, username):
        username_textbox = self.find(By.XPATH, "//input[@name='username']")
        username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = self.find(By.XPATH, "//input[@name='password']")
        password_textbox.send_keys(password)

    def click_login(self):
        self.click(By.XPATH, "//button[@type='submit']")
     