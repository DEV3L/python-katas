from kata_template.fizz_buzz.fizz_buzz import fizz_buzz

def test_fizz_buzz_empty():
    expected_result = []

    fizz_buzz_results = fizz_buzz(0)

    assert expected_result == fizz_buzz_results

def test_fizz_buzz_one():
    expected_result = [1]

    fizz_buzz_results = fizz_buzz(1)

    assert expected_result == fizz_buzz_results

def test_fizz_buzz_two():
    expected_result = [1,2]

    fizz_buzz_results = fizz_buzz(2)

    assert expected_result == fizz_buzz_results
