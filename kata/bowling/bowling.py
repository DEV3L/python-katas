def score_game(frames: list):
    score = 0
    for frame in frames:
        score += sum(frame)
    return score
