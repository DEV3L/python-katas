from unittest.mock import patch


@patch('builtins.print')
def test_hello_world(mock_print):
    import hello_world.iteration_a.hello_world
    mock_print.assert_called_with('hello world')
