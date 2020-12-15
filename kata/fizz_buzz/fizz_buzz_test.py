from kata.fizz_buzz.fizz_buzz import fizz_buzz


def test_fizz_buzz_one():
    expected_value = [1]

    result = fizz_buzz(1)

    assert expected_value == result


def test_fizz_buzz_three():
    expected_value = [1, 2, 'Fizz']

    result = fizz_buzz(3)

    assert expected_value == result


def test_fizz_buzz_five():
    expected_value = [1, 2, 'Fizz', 4, 'Buzz']

    result = fizz_buzz(5)

    assert expected_value == result


def test_fizz_buzz_fifteen():
    expected_value = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

    result = fizz_buzz(15)

    assert expected_value == result
