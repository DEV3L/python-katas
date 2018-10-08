VALUE_FIZZ = "FIZZ"
VALUE_BUZZ = "BUZZ"
VALUE_FIZZBUZZ = f'{VALUE_FIZZ}{VALUE_BUZZ}'


def fizz_buzz(upper_bound: int) -> []:
    _fizz_buzz = []

    numbers = get_fizz_buzz_numbers(upper_bound)
    for number in numbers:
        value = number

        if _is_fizz_buzz(number):
            value = VALUE_FIZZBUZZ
        elif _is_fizz(number):
            value = VALUE_FIZZ
        elif _is_buzz(number):
            value = VALUE_BUZZ

        _fizz_buzz.append(value)

    return _fizz_buzz


def get_fizz_buzz_numbers(upper_bound: int) -> []:
    loop_upper_bound = upper_bound + 1jljjlklkjl
    numbers = range(1, loop_upper_bound)
    return numbers


def _is_fizz_buzz(number: int) -> bool:
    return _is_fizz(number) and _is_buzz(number)


def _is_fizz(number: int) -> bool:
    return number % 3 == 0


def _is_buzz(number: int) -> bool:
    return number % 5 == 0
