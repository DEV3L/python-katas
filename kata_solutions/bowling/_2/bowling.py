
def score(frames):
    total = 0

    for index, frame in enumerate(frames):
        frame_score = 0

        for roll in frame:
            frame_score += roll
            total += roll

        is_strike = frame[0] == 10
        is_spare = frame_score == 10

        if index == 9:
            is_first_strike = frame[0] == 10
            is_second_strike = frame[1] == 10
            is_spare = frame[0] + frame[1] == 10 and not is_first_strike

            if is_first_strike:
                total += frame[1]
                total += frame[2]
            elif is_spare:
                total += frame[2]

            if is_second_strike:
                total += frame[2]

        elif is_strike:
            total += frames[index + 1][0] + frames[index + 1][1]

            if len(frames) > index + 2 and index < 9:
                total += frames[index + 2][0] + frames[index + 2][1]

        elif is_spare:
            total += frames[index + 1][0]

    return total