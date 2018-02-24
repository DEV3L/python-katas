from unittest.mock import MagicMock

from pytest import fixture


@fixture(name='browser_client')
def _browser_client():
    browser_client = MagicMock()
    return browser_client