from app.actions._action import Action
from app.config import github_login_url, github_username, github_password


class LogIntoGitHub(Action):
    def execute(self, *, github_url=github_login_url):
        self.browser_client.get(github_url)
        self.browser_client.set_text_value(github_username, id='login_field')
        self.browser_client.set_text_value(github_password, id='password')
        self.browser_client.click_button(name='commit')
