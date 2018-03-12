def parse_string_time(input_time: str) -> float:
    total_amount = 0

    times = _slice_input_times(input_time)

    for _amount, duration_type in times:
        amount = _to_float(_amount)
        multiplier = _parse_multiplier(duration_type)
        total_amount += amount * multiplier

    return total_amount


def _parse_multiplier(duration_type):
    multiplier = 0
    if 'ms' == duration_type:
        multiplier = .001
    elif 'sec' == duration_type:
        multiplier = 1
    elif 'min' == duration_type:
        multiplier = 60
    elif 'hr' == duration_type:
        multiplier = 60
    return multiplier


def _slice_input_times(input_time: str) -> iter:
    input_time_chunks = iter(input_time.split(' '))
    input_time_tuples = zip(input_time_chunks, input_time_chunks)
    return input_time_tuples


def _to_float(amount: str) -> float:
    try:
        amount = float(amount)
    except:
        amount = 0.0

    return amount
