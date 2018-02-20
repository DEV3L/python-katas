ALL_PINS = 10
LAST_ROUND = 9


class Frame:
    ALL_PINS = 10

    def __init__(self, rolls: tuple):
        self.first_roll = rolls[0]
        self.second_roll = rolls[1]
        self.third_roll = rolls[2] if len(rolls) == 3 else 0

    @property
    def score(self):
        return self.first_roll + self.second_roll + self.third_roll

    @property
    def is_strike(self):
        return self.first_roll == self.ALL_PINS

def score_game(frames: list):
    score = 0

    for round_number, rolls in enumerate(frames):
        frame = Frame(rolls)

        is_spare = _is_spare(rolls[:2])
        is_strike = frame.is_strike

        score += frame.score

        if not is_spare and not is_strike:
            continue

        if round_number >= LAST_ROUND:
            continue

        next_roll_frame = frames[round_number + 1]
        score += next_roll_frame[0]

        if is_strike:
            if next_roll_frame[0] == ALL_PINS and round_number != LAST_ROUND - 1:
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
