ALL_PINS = 10
LAST_ROUND = 10


def score_game(frame_rolls: list):
    score = 0

    frames = [Frame(round_number, rolls) for round_number, rolls in enumerate(frame_rolls, start=1)]

    for round_number, frame in enumerate(frames, start=1):
        next_roll = get_frame(frames, round_number)
        second_next_roll = get_frame(frames, round_number + 1)

        score += frame.score(next_roll, second_next_roll)

    return score


def get_frame(frames, round_number):
    next_roll = frames[round_number] if round_number < LAST_ROUND else None
    return next_roll


class Frame:
    SECOND_LAST_ROUND = 9
    ALL_PINS = 10

    def __init__(self, round_number: int, rolls: tuple):
        self.round_number = round_number
        self._rolls = rolls

        self.first_roll = rolls[0]
        self.second_roll = rolls[1]
        self.third_roll = rolls[2] if len(rolls) == 3 else 0

    @property
    def is_strike(self):
        return self._is_all_pins(self.first_roll)

    @property
    def is_spare(self):
        return not self.is_strike and self._is_all_pins(self.first_roll + self.second_roll)

    def score(self, next_frame: 'Frame', second_next_frame: 'Frame'):
        score = self.first_roll + self.second_roll + self.third_roll

        if (self.is_spare or self.is_strike) and next_frame:
            score += next_frame.first_roll

        if self.is_strike and next_frame:
            if next_frame.is_strike and self.round_number != self.SECOND_LAST_ROUND:
                score += second_next_frame.first_roll
            else:
                score += next_frame.second_roll

        return score

    @classmethod
    def _is_all_pins(self, score):
        return score == self.ALL_PINS
