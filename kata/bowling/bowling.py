ALL_PINS = 10
LAST_ROUND = 10
SECOND_LAST_ROUND = 9


def score_game(frame_rolls: list):
    score = 0

    frames = [Frame(rolls) for rolls in frame_rolls]

    for index, frame in enumerate(frames):
        round_number = index + 1
        next_roll = get_frame(frames, round_number)
        second_next_roll = frames[index + 2] if round_number < SECOND_LAST_ROUND else None

        score += frame.score(next_roll, second_next_roll)

    for index, rolls in enumerate(frame_rolls):
        round_number = index + 1
        frame = Frame(rolls)
        next_rolls = get_frame(frame_rolls, round_number)

        if not next_rolls:
            continue

        if frame.is_strike:
            score += next_rolls[0]
            if next_rolls[0] == ALL_PINS and index != 9 - 1:
                second_roll = frame_rolls[index + 2][0] if index < 9 - 1 else 0
            else:
                second_roll = frame_rolls[index + 1][1]
            score += second_roll
        elif frame.is_spare:
            score += next_rolls[0]
    return score


def get_frame(frames, round_number):
    next_roll = frames[round_number] if round_number < LAST_ROUND else None
    return next_roll


class Frame:
    TOTAL_ROUND = 10
    ALL_PINS = 10

    def __init__(self, rolls: tuple):
        self._rolls = rolls

        self.first_roll = rolls[0]
        self.second_roll = rolls[1]
        self.third_roll = rolls[2] if len(rolls) == 3 else 0

    def score(self, next_frame, second_next_frame):
        return self.first_roll + self.second_roll + self.third_roll

    @property
    def is_strike(self):
        return self._is_all_pins(self.first_roll)

    @property
    def is_spare(self):
        return not self.is_strike and self._is_all_pins(self.score(None, None))

    @classmethod
    def _is_all_pins(self, score):
        return score == self.ALL_PINS
