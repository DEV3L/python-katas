from kata_solutions.fizz_buzz._4.fizz_buzz import fizz_buzz

"""
user picks a number
display a list from 1 to the user selected number
if evenly divisible by 3, replace "FIZZ"
if evenly divisible by 5, replace "BUZZ"
if both, replace FIZZBUZZ
"""


def test_fizz_buzz_init():
    expected_length = 1

    result = fizz_buzz(1)

    assert expected_length == len(result)


def test_fizz_two():
    expected_result = [1, 2]

    result = fizz_buzz(2)

    assert expected_result == result


def test_fizz_buzz_fizz():
    expected_result = [1, 2, "FIZZ"]

    result = fizz_buzz(3)

    assert expected_result == result


def test_fizz_buzz_buzz():
    expected_result = [1, 2, "FIZZ", 4, "BUZZ"]

    result = fizz_buzz(5)

    assert expected_result == result


def test_fizz_buzz_fizzbuzz():
    expected_result = [1, 2, "FIZZ", 4, "BUZZ", "FIZZ", 7, 8, "FIZZ", "BUZZ", 11, "FIZZ", 13, 14, "FIZZBUZZ"]

    result = fizz_buzz(15)

    assert expected_result == result
