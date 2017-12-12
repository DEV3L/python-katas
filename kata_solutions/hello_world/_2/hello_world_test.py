from unittest.mock import patch


@patch('builtins.print')
def test_hello_world(mock_print):
    mock_print.assert_called_with('hello world')
