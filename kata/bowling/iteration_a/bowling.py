class Bowling():
    def __init__(self, frames):
        self.frames = frames

    def score_game(self):
        score = 0
        for frame in self.frames:
            score += frame[0] + frame[1]
        return score
