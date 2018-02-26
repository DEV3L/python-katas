from unittest.mock import patch

from app.services.pickle_service import load_pickle_data, write_pickle_data, serialize


@patch('app.services.pickle_service.open')
@patch('app.services.pickle_service.pickle')
def test_load_pickle_data(mock_pickle, mock_open):
    expected_unpickled_object = mock_pickle.load.return_value

    unpickled_object = load_pickle_data('path')

    assert expected_unpickled_object == unpickled_object
    mock_open.assert_called_with('path', 'rb')
    mock_pickle.load.assert_called_with(mock_open.return_value)


@patch('app.services.pickle_service.open')
@patch('app.services.pickle_service.pickle')
def test_write_pickle_data(mock_pickle, mock_open):
    write_pickle_data('object', 'path')

    mock_open.assert_called_with('path', 'wb')
    mock_pickle.dump.assert_called_with('object', mock_open.return_value)


@patch('app.services.pickle_service.pickle.dumps')
def test_serialize(mock_dumps):
    mock_dumps.return_value = b'value'
    value = "value"

    byte_value = serialize(value)

    assert bytes(value, encoding='UTF-8') == byte_value
