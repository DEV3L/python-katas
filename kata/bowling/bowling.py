def score_game(frames: list):
    score = 0

    for round_number, frame in enumerate(frames):
        is_spare = False

        round_score = sum(frame)
        score += round_score

        if round_score == 10:
            is_spare = True

        if is_spare and round_number < 9:
            score += frames[round_number + 1][0]

    return score
