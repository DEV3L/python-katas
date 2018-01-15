def fizz_buzz(upper_bound):
    return_str = ''

    for number in range(upper_bound):
        _number = number + 1
        if return_str:
            return_str += ','

        if (_number % 3 == 0):
            return_str += 'fizz'
        else:
            return_str += str(_number)

    return return_str
