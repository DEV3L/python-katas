# ZOMBIES

"""
|'1 ms'  | .001 |
|'1 sec' | 1 |
|'1 min' | 60 |
|'1 hr'  | 3600 |
|'5 sec 421 ms' | 5.421 |
|'9 min 57 sec' | 597 |
|'1 hr 33 min'  | 5580 |
|'1 hr 1 min 1 sec 111 ms' | 3661.111 |
|'' | 0 |
"""
from pytest import mark

from kata.parse_string_time.parse_string_time import parse_string_time


@mark.parametrize('input_value, expected_value', [
    ('1 sec', 1)
])
def test_seconds(input_value, expected_value):
    time_value = parse_string_time(input_value)
    assert expected_value == time_value
