from app.actions._action import Action
from app.clients.browser_client import BrowserClient
from app.config import jenkins_url
from selenium.webdriver.common.by import By

base_url = f'{jenkins_url}view/OnShift-OnShift/job/OnShift-OnShift/job/'
build_numbers_css_selector = 'a.tip.model-link.inside.build-link.display-name.zws-inserted'

class FetchBuildNumbersForBranch(Action):
    def __init__(self, browser_client: BrowserClient, branch_name: str):
        super().__init__(browser_client)
        self.branch_name = branch_name

    @property
    def branch_url(self):
        branch_url = f'{base_url}{self.branch_name}'
        return branch_url

    def execute(self):
        self.browser_client.get(self.branch_url)

        build_number_elements = self.browser_client.find_elements_by_css_selector(
            build_numbers_css_selector)

        build_numbers = [self._clean_build_number(build_number.text) for build_number in build_number_elements]
        return build_numbers

    @staticmethod
    def _clean_build_number(build_number_text):
        build_number = build_number_text.replace('#', '').split('-')[0]
        return int(build_number)