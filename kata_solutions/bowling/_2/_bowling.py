
def score(frames):
    total = 0

    is_spare = False
    is_strike = False

    for count, frame in enumerate(frames):
        if is_spare:
            total += frame[0]

        frame_score = 0
        for roll in frame:
            frame_score += roll
            total += roll

        if is_strike:
            total += frame_score
            is_strike = False

        if frame[0] == 10:
            is_strike = True
        elif frame_score == 10:
            is_spare = True

    return total