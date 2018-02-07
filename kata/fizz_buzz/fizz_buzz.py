def fizz_buzz(upper_bound):
    fizz_buzz_range = [index + 1 for index in range(upper_bound)]

    for count in fizz_buzz_range:
        value = ''

        if count % 3 == 0:
            value = 'Fizz'

        if count % 5 == 0:
            value += 'Buzz'

        value = value or str(count)

        set_value(fizz_buzz_range, value, count)

    return fizz_buzz_range


def set_value(fizz_buzz_range, value, count):
    index = count - 1
    fizz_buzz_range[index] = value

# def fizz_buzz(upper_bound):
#     fizz_buzz_list = []
#
#     for index in range(upper_bound):
#         count = index + 1
#
#         if count % 15 == 0:
#             fizz_buzz_list.append('FizzBuzz')
#         elif count % 3 == 0:
#             fizz_buzz_list.append('Fizz')
#         elif count % 5 == 0:
#             fizz_buzz_list.append('Buzz')
#         else:
#             fizz_buzz_list.append(str(count))
#
#     return fizz_buzz_list
