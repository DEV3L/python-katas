from app.actions._action import Action
from app.config import jenkins_url


class LogIntoJenkins(Action):
    def execute(self, *, jenkins_url=jenkins_url):
        self.browser_client.get(jenkins_url)
        self.browser_client.navigate_link('Log in')
