from unittest.mock import patch


class SuperClass(object):
    def __init__(self):
        print('called super init')


class ChildClass(SuperClass):
    def __init__(self):
        super(ChildClass, self).__init__()
        print('called child init')


@patch('builtins.print')
def test_super_and_child_call_init(mock_print):
    ChildClass()

    assert 2 == mock_print.call_count


@patch('builtins.print')
@patch('sandbox.mock_super_init.SuperClass.__init__')
def test_child_does_not_call_super_init_when_mocked(mock_super_class, mock_print):
    ChildClass()

    assert mock_super_class.called
    assert 1 == mock_print.call_count
