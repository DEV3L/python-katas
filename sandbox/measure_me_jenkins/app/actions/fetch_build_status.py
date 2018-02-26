from app.actions._action import Action
from app.clients.browser_client import BrowserClient
from app.config import jenkins_url

base_console_url = f'{jenkins_url}view/OnShift-OnShift/job/OnShift-OnShift/job/'

class FetchBuildStatus(Action):
    def __init__(self, browser_client: BrowserClient, branch_name: str, build_number: int):
        super().__init__(browser_client)
        self.branch_name = branch_name
        self.build_number = build_number

    @property
    def console_url(self):
        console_url = f'{base_console_url}{self.branch_name}/{self.build_number}/console'
        return console_url
