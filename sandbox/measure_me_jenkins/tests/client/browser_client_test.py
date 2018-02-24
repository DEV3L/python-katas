from unittest.mock import MagicMock

from app.clients.browser_client import BrowserClient
from pytest import fixture


@fixture(name='webdriver')
def _webdriver():
    mock_webdriver = MagicMock()
    return mock_webdriver

@fixture(name='browser_client')
def _browser_client(webdriver):
    browser_client = BrowserClient(webdriver)
    assert webdriver == browser_client.webdriver

    return browser_client


def test_get_url(browser_client):
    expected_url = 'some_url'

    browser_client.get(expected_url)

    browser_client.webdriver.get.assert_called_with(expected_url)

def test_navigate_link(browser_client):
    expected_link_text = 'link_text'

    browser_client.navigate_link(expected_link_text)

    browser_client.webdriver.find_element_by_link_text.assert_called_with(expected_link_text)
    assert browser_client.webdriver.find_element_by_link_text.return_value.click.called


def test_set_text_field(browser_client):
    expected_element_id = 'element_id'
    expected_set_value = 'set_value'

    browser_client.set_text_value(expected_set_value, id=expected_element_id)

    browser_client.webdriver.find_element_by_id.assert_called_with(expected_element_id)
    browser_client.webdriver.find_element_by_id.return_value.send_keys.assert_called_with(expected_set_value)


def test_click_button(browser_client):
    expected_button_name = 'button'

    browser_client.click_button(name=expected_button_name)

    browser_client.webdriver.find_element_by_name.assert_called_with(expected_button_name)
    assert browser_client.webdriver.find_element_by_name.return_value.click.called

