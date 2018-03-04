# ZOMBIES

"""
|'1 ms'  | .001 |
|'1 hr'  | 3600 |
|'5 sec 421 ms' | 5.421 |
|'9 min 57 sec' | 597 |
|'1 hr 33 min'  | 5580 |
|'1 hr 1 min 1 sec 111 ms' | 3661.111 |
"""
from pytest import mark

from kata.parse_string_time.parse_string_time import parse_string_time


@mark.parametrize('input_value, expected_value', [
    # seconds
    ('1 sec', 1),
    ('2 sec', 2),
    ('3 sec', 3),
    # minutes
    ('1 min', 60),
    ('3 min', 180),
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
