from app.actions.fetch_build_numbers_for_branch import FetchBuildNumbersForBranch
from app.actions.log_into_github import LogIntoGitHub
from app.actions.log_into_jenkins import LogIntoJenkins
from app.clients.browser_client import BrowserClient
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

if __name__ == '__main__':

    try:
        chrome_webdriver = ChromeWebDriver()
        browser_client = BrowserClient(chrome_webdriver)

        log_into_github = LogIntoGitHub(browser_client)
        log_into_github.execute()

        log_into_jenkins = LogIntoJenkins(browser_client)
        log_into_jenkins.execute()

        fetch_build_information_for_branch = FetchBuildNumbersForBranch(browser_client, 'master')
        fetch_build_information_for_branch.execute()
    except:
        chrome_webdriver.close()
    else:
        chrome_webdriver.close()