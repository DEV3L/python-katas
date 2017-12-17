from kata_solutions.bowling._2.bowling import score


# zombies
# zero
# one
# many
# boundaries - 10th frame
# interface
# exceptional - spare / strike
# simple
#
def test_score_zeros():
    # 0x
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 0 == bowling_score


def test_score_one():
    # 1, 0x
    frames = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ]

    bowling_score = score(frames)

    assert 1 == bowling_score


def test_scores_no_strike_no_spare():
    # 9, 9, 9, 9, 9, 9, 9, 9, 9, 9
    frames = [[5, 4], [5, 4], [5, 4], [5, 4], [5, 4], [5, 4], [5, 4], [5, 4], [5, 4], [5, 4]]

    bowling_score = score(frames)

    assert 90 == bowling_score


def test_spare_zero_next():
    # 10, 0x
    frames = [[1, 9], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 10 == bowling_score


def test_spare_not_zero_next():
    # 11, 1, 0x
    frames = [[1, 9], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 12 == bowling_score


def test_spare_multiple_spares():
    # 11, 11, 10, 0x
    frames = [[1, 9], [1, 9], [1, 9], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 32 == bowling_score


def test_all_spare_except_last_frame():
    # 11, 11, 11, 11, 11, 11, 11, 11, 10, 0
    frames = [[1, 9], [1, 9], [1, 9], [1, 9], [1, 9], [1, 9], [1, 9], [1, 9], [1, 9], [0, 0]]

    bowling_score = score(frames)

    assert 98 == bowling_score


def test_strike_zero_frame_next():
    # 10, 0x
    frames = [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 10 == bowling_score


def test_strike_score_frame_next_zero_next():
    # 12, 2, 0x
    frames = [[10, 0], [1, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 14 == bowling_score


def test_strike_score_frame_next_score_next():
    # 22, 2, 10, 0x
    frames = [[10, 0], [1, 1], [1, 9], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 34 == bowling_score


def test_three_strikes_in_a_row():
    # 30, 20, 10
    frames = [[10, 0], [10, 0], [10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 60 == bowling_score


def test_ninth_frame_strike_zero_next():
    # 0, 0, 0, 0, 0, 0, 0, 0, 10, 0
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 0], [0, 0]]

    bowling_score = score(frames)

    assert 10 == bowling_score


def test_tenth_frame_no_strike_no_spare():
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 9
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [9, 0]]

    bowling_score = score(frames)

    assert 9 == bowling_score


def test_tenth_frame_spare():
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [9, 1, 1]]

    bowling_score = score(frames)

    assert 12 == bowling_score


def test_tenth_frame_strike():
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, (12, 1, 1)
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 1, 1]]

    bowling_score = score(frames)

    assert 14 == bowling_score


def test_tenth_frame_strike_spare():
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, (20, 9, 1)
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 9, 1]]

    bowling_score = score(frames)

    assert 30 == bowling_score


def test_tenth_frame_strik_strike_zero():
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, (20, 10, 0)
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 10, 0]]

    bowling_score = score(frames)

    assert 30 == bowling_score


def test_tenth_frame_strik_strike_strike():
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, (30, 20, 10)
    frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 10, 10]]

    bowling_score = score(frames)

    assert 60 == bowling_score


def test_eight_strikes():
    # 1-30, 2-30, 3-30, 4-30, 5-30, 6-30, 7-20, 8-10, 9-0, 10-0
    frames = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [0, 0], [0, 0]]

    bowling_score = score(frames)

    assert 210 == bowling_score


def test_nine_strikes():
    # 1-30, 2-30, 3-30, 4-30, 5-30, 6-30, 7-30, 8-20, 9-10, 10-0
    frames = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [0, 0]]

    bowling_score = score(frames)

    assert 240 == bowling_score


def test_ten_strikes():
    # 1-30, 2-30, 3-30, 4-30, 5-30, 6-30, 7-30, 8-30, 9-20, 10-10
    frames = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0, 0]]

    bowling_score = score(frames)

    assert 270 == bowling_score


# def test_eleven_strikes():
#     # 1-30, 2-30, 3-30, 4-30, 5-30, 6-30, 7-30, 8-30, 9-30
#     frames = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 10, 0]]
#
#     bowling_score = score(frames)
#
#     assert 290 == bowling_score

# Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game. Here are some things that the program will not do:

# We can briefly summarize the scoring for this form of bowling:
#
# If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and
# his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.
#
# If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
#
# The game score is the total of all frame scores.
