"""
Z - zero
O - one
M - many
B - boundary behaviors
I - interface definition
E - exercise exceptional behavior
S - Simple scenarios, simple solutions
"""

from kata_solutions.fizz_buzz._2.fizz_buzz import fizz_buzz


def test_fizz_buzz_one():
    upper_bound = 1
    assert '1' == fizz_buzz(upper_bound)


def test_fizz_buzz_two():
    upper_bound = 2
    assert '1,2' == fizz_buzz(upper_bound)


def test_fizz_buzz_three():
    upper_bound = 3
    assert '1,2,fizz' == fizz_buzz(upper_bound)
