def score_game(frames):
    total = 0

    for index, frame in enumerate(frames):
        # frame => (10, 0) # 14, frame+1 => (2, 2) # 4
        frame_total = sum(frame)

        if frame[0] == 10:
            total += sum(frames[index + 1])
            # if frames[index + 2][0] == 10:
            #     total += frames[index + 2][0]

        elif frame_total == 10:
            total += frames[index + 1][0]

        total += frame_total

    return total
