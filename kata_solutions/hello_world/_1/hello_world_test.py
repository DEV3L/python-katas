from unittest.mock import patch


@patch('builtins.print')
def test_hello_world(mock_print):
    import kata_solutions.hello_world._1.hello_world
    mock_print.assert_called_with('hello world')
