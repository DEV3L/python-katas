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
