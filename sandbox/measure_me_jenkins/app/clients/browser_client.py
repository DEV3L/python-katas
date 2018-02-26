from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BrowserClient:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def get(self, url):
        self.webdriver.get(url)

    def navigate_link(self, link_text):
        link_element = self.webdriver.find_element_by_link_text(link_text)
        link_element.click()

    def set_text_value(self, value, *, id=None):
        text_element = self.webdriver.find_element_by_id(id)
        text_element.send_keys(value)

    def click_button(self, *, name=None):
        button_element = self.webdriver.find_element_by_name(name)
        button_element.click()

    def find_elements_by_css_selector(self, css_selector: str):
        return self.webdriver.find_elements(By.CSS_SELECTOR, css_selector)

    def find_element_by_class_name(self, class_name):
        return self.webdriver.find_element_by_class_name(class_name)
