import itertools

from pytest import fixture
from pytest import mark

from kata.bowling.bowling import score_game


@fixture(name='frames')
def _frames():
    frames = list(itertools.repeat((0, 0), 10))
    return frames


@mark.parametrize('expected_score, scores', [
    (0, []),
    (1, [(1, 0)]),
    (10, [(1, 9)]),
    (10, [(10, 0)]),
    (10, list(itertools.repeat((1, 0), 10))),
    (30, list(itertools.repeat((1, 2), 10)))
])
def test_score(expected_score, scores, frames):
    _substitute_frame_scores(frames, scores)

    score = score_game(frames)
    assert expected_score == score


@mark.parametrize('expected_score, scores', [
    (12, [(1, 9), (1, 0)]),
    (30, [(1, 9), (10, 0)]),
    (36, [(1, 9), (2, 8), (7, 0)]),
])
def test_spare(expected_score, scores, frames):
    _substitute_frame_scores(frames, scores)

    score = score_game(frames)
    assert expected_score == score


def test_strike_one_zero(frames):
    frames[0] = (10, 0)
    frames[1] = (1, 0)

    expected_value = 12
    score = score_game(frames)

    assert expected_value == score


def test_strike_one_one(frames):
    frames[0] = (10, 0)
    frames[1] = (1, 1)

    expected_value = 14
    score = score_game(frames)

    assert expected_value == score


def test_strike_strike_one(frames):
    frames[0] = (10, 0)
    frames[1] = (10, 0)
    frames[2] = (1, 0)

    expected_value = 33
    score = score_game(frames)

    assert expected_value == score

def _substitute_frame_scores(frames, scores):
    for index, score in enumerate(scores):
        frames[index] = score


# ZOMBIES
# Zero
# One
# Many
# Boundaries
# Interfaces
# Exceptions
# Simple

"""
Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling,
produces the total score for the game. Here are some things that the program will not do:


If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.

The game score is the total of all frame scores.



"""
