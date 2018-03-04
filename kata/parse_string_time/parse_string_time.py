def parse_string_time(input_time: str) -> float:
    try:
        return _parse_string_time(input_time)
    except:
        return 0


def _parse_string_time(input_time: str) -> float:
    amount = int(input_time.split(' ')[0])
    duration_type = input_time.split(' ')[1]

    multiplier = 0
    if 'min' == duration_type:
        multiplier = 60
    elif 'sec' == duration_type:
        multiplier = 1

    return amount * multiplier
