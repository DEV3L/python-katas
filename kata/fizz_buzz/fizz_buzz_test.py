from pytest import mark

from kata.fizz_buzz.fizz_buzz import fizz_buzz


# ZOMBIES
# Zero One Many
# Boundaries Interfaces Edges Simple

def test_fizz_buzz_zero():
    expected_value = []

    value = fizz_buzz(0)

    assert expected_value == value


def test_fizz_buzz_one():
    expected_value = ['1']

    value = fizz_buzz(1)

    assert expected_value == value


@mark.parametrize('expected_value, upper_bound', [
    (['1', '2'], 2),
    (['1', '2', 'Fizz'], 3),
    (['1', '2', 'Fizz', '4'], 4),
    (['1', '2', 'Fizz', '4', 'Buzz'], 5),
    (['1', '2', 'Fizz', '4', 'Buzz', 'Fizz'], 6),
    (['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'], 10),
    (['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'], 15),
    (['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz',
      '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz'], 30),
])
def test_fizz_buzz(expected_value, upper_bound):
    value = fizz_buzz(upper_bound)

    assert expected_value == value
