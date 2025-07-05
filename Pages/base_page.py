
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # def open_url(self, url):
    #     self.driver.get(url)

    def find(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
    


    def click(self, by, value):
        self.find(by, value).click()

    # def send_keys(self, by, value, text):
    #     self.find(by, value).send_keys(text)

    # def get_title(self):
    #     return self.driver.title

    # def current_url(self):
    #     return self.driver.current_url

    