def fizz_buzz(upper_bound):
    fizz_buzz_list = []

    for index in range(upper_bound):
        count = index + 1

        if count % 15 == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif count % 3 == 0:
            fizz_buzz_list.append('Fizz')
        elif count % 5 == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(str(count))

    return fizz_buzz_list
