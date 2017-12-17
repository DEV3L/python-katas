from pytest import fixture

from kata_solutions.bowling._3.bowling import score_game


@fixture(name="frame")
def _frame():
    return [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]


# zombies
# zero
# one
# many (complicated)
# boundaries (edges) -- preconditions
# interfaces
# exceptional - strikes, spares, 10th frame
# simple

# If in two tries, he fails to knock them all down, his score for that frame is the total
#   number of pins knocked down in his two tries.

def test_zero_score(frame):
    final_score = score_game(frame)

    assert 0 == final_score


def test_frame_one_score_one(frame):
    frames = frame
    frames[0] = (1, 0)

    final_score = score_game(frames)

    assert 1 == final_score


def test_scores_no_strike_no_spares(frame):
    frames_score_two = list(frame)
    frames_score_two[0] = (1, 1)
    final_score = score_game(frames_score_two)

    assert 2 == final_score

    frames_score_all_one = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
    final_score = score_game(frames_score_all_one)
    assert 20 == final_score


# If in two tries he knocks them all down, this is called a “spare” and his
# score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).


def test_frame_one_spare_rest_empty(frame):
    frame[0] = (8, 2)

    final_score = score_game(frame)

    assert 10 == final_score


def test_frame_one_spare_frame_two_score(frame):
    frame[0] = (8, 2)  # 11
    frame[1] = (1, 0)  # 1

    final_score = score_game(frame)

    assert 12 == final_score

    frame[0] = (8, 2)  # 18
    frame[1] = (8, 2)  # 10

    final_score = score_game(frame)

    assert 28 == final_score

    frame[0] = (0, 10)  # 18
    frame[1] = (8, 2)  # 10

    final_score = score_game(frame)

    assert 28 == final_score

    frame[0] = (0, 10)  # 20
    frame[1] = (10, 0)  # 10

    final_score = score_game(frame)

    assert 30 == final_score


# If on his first try in the frame he knocks down all the pins, this is called a “strike”.
# His turn is over, and his score for the frame is ten plus the simple total of the pins
# knocked down in his next two rolls.

def test_frame_one_strike_zeros(frame):
    frame[0] = (10, 0)

    final_score = score_game(frame)

    assert 10 == final_score


def test_frame_one_strike_frame_two_score(frame):
    frame[0] = (10, 0)  # 14
    frame[1] = (2, 2)  # 4

    final_score = score_game(frame)

    assert 18 == final_score

    frame[0] = (10, 0)  # 20
    frame[1] = (9, 1)  # 10

    final_score = score_game(frame)

    assert 30 == final_score

# def test_two_strikes_and_score(frame):
#     frame[0] = (10, 0)
#     frame[1] = (10, 0)
#     frame[2] = (1, 1)
#
#     final_score = score_game(frame)
#
#     assert 35 == final_score

# If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
# The game score is the total of all frame scores.
