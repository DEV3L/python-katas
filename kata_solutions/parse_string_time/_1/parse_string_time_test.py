from pytest import mark

from kata_solutions.parse_string_time._1.parse_string_time import parse_string_time


@mark.parametrize('input_value, expected_value', [
    # milliseconds
    ('1 ms', .001),
    ('2 ms', .002),
    ('419 ms', .419),
    # seconds
    ('1 sec', 1),
    ('2 sec', 2),
    ('3 sec', 3),
    # minutes
    ('1 min', 60),
    ('3 min', 180),
    # hours
    ('1 hr', 60),
    ('3 hr', 180),
    # joined
    ('3 hr 5 sec', 185),
    ('1 hr 1 ms', 60.001),
    # invalid
    ('x sec', 0),
    ('', 0),
    ('1 se', 0),
    ('10 minute', 0),
    ('5', 0)
])
def test_parse_string_time(input_value, expected_value):
    time_value = parse_string_time(input_value)
    assert expected_value == time_value
