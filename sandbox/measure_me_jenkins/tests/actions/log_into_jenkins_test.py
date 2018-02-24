from app.actions.log_into_jenkins import LogIntoJenkins
from app.config import jenkins_url


def test_log_into_jenkins_execute(browser_client):
    log_into_jenkis = LogIntoJenkins(browser_client)

    log_into_jenkis.execute()

    browser_client.get.assert_called_with(jenkins_url)
    browser_client.navigate_link.assert_called_with('Log in')
