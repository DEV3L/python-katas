from unittest.mock import MagicMock

from app.actions.fetch_build_numbers_for_branch import FetchBuildNumbersForBranch, base_url, build_numbers_css_selector


def test_fetch_build_numbers_for_branch_test(browser_client):
    expected_branch_name = 'branch'
    expected_branch_url = base_url + expected_branch_name

    fetch_build_information_for_branch = FetchBuildNumbersForBranch(browser_client, expected_branch_name)

    assert expected_branch_name == fetch_build_information_for_branch.branch_name
    assert browser_client == fetch_build_information_for_branch.browser_client
    assert expected_branch_url == fetch_build_information_for_branch.branch_url


def test_fetch_build_numbers_for_branch_execute(browser_client):
    expected_build_numbers = [1, 2, 3]
    expected_branch_name = 'branch'
    expected_branch_url = base_url + expected_branch_name

    fetch_build_numbers_for_branch = FetchBuildNumbersForBranch(browser_client, expected_branch_name)

    mock_find_elements_by_css_selector_return_value = [
        MagicMock(text='#1'), MagicMock(text='#2-Information'), MagicMock(text='#3')
    ]
    browser_client.find_elements_by_css_selector.return_value = \
        mock_find_elements_by_css_selector_return_value

    build_numbers = fetch_build_numbers_for_branch.execute()

    mock_browser_client = fetch_build_numbers_for_branch.browser_client
    mock_browser_client.get.assert_called_with(expected_branch_url)
    mock_browser_client.find_elements_by_css_selector. \
        assert_called_with(build_numbers_css_selector)

    assert expected_build_numbers == build_numbers
