from app.actions.log_into_github import LogIntoGitHub
from app.actions.log_into_jenkins import LogIntoJenkins
from app.clients.browser_client import BrowserClient
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

if __name__ == '__main__':
    chrome_webdriver = ChromeWebDriver()
    browser_client = BrowserClient(chrome_webdriver)

    log_into_github = LogIntoGitHub(browser_client)
    log_into_github.execute()

    log_into_jenkins = LogIntoJenkins(browser_client)
    log_into_jenkins.execute()
