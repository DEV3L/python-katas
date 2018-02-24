from app.clients.browser_client import BrowserClient


class Action:
    def __init__(self, browser_client: BrowserClient):
        self.browser_client = browser_client
