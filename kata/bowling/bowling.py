ALL_PINS = 10
LAST_ROUND = 9


def score_game(frames: list):
    score = 0

    for round_number, frame in enumerate(frames):
        score += sum(frame)

        is_spare = _is_spare(frame)
        is_strike = _is_strike(frame)

        if not is_spare and not is_strike:
            continue

        if round_number >= LAST_ROUND:
            continue

        next_roll_frame = frames[round_number + 1]
        score += next_roll_frame[0]

        if is_strike:
            if next_roll_frame[0] == ALL_PINS:
                second_roll = frames[round_number + 2][0] if round_number < LAST_ROUND - 1 else 0
            else:
                second_roll = frames[round_number + 1][1]

            score += second_roll

    return score


def _is_spare(frame: tuple):
    round_score = sum(frame)

    if frame[0] != ALL_PINS \
            and round_score == ALL_PINS:
        return True
    return False


def _is_strike(frame: tuple):
    return frame[0] == ALL_PINS
