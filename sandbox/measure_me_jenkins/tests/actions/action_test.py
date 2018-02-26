from unittest.mock import MagicMock

from app.actions._action import Action
from app.actions.log_into_jenkins import LogIntoJenkins
from app.clients.browser_client import BrowserClient
from app.config import jenkins_url
from pytest import fixture


@fixture(name='browser_client')
def _browser_client():
    browser_client = MagicMock()
    return browser_client


def test_log_into_jenkins_init(browser_client):
    action = Action(browser_client)

    assert browser_client == action.browser_client
