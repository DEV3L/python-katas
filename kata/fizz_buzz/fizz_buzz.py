def fizz_buzz(input):
    result = []
    for x in range(1, input + 1):
        value = ''

        if x % 3 == 0:
            value += 'Fizz'
        if x % 5 == 0:
            value += 'Buzz'

        value = value or x

        result.append(value)

    return result
