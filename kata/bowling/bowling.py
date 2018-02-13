def score_game(frames: list):
    score = 0

    for round_number, frame in enumerate(frames):
        is_spare = False
        is_strike = False

        round_score = sum(frame)
        score += round_score

        if round_score == 10:
            is_spare = True
            if frame[0] == 10:
                is_strike = True

        next_roll = frames[round_number + 1][0] if round_number < 9 else 0
        if is_strike:
            score += next_roll

            if next_roll == 10:
                second_roll = frames[round_number + 2][0] if round_number < 8 else 0
            else:
                second_roll = frames[round_number + 1][1] if round_number < 9 else 0

            score += second_roll
        elif is_spare:
            score += next_roll


    return score
