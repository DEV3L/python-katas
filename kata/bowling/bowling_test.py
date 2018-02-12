# ZOMBIES
# Zero
# One
# Many
# Boundaries
# Interfaces
# Exceptions
# Simple

# bowling kata
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
    for index, score in enumerate(scores):
        frames[index] = score

    score = score_game(frames)
    assert expected_score == score


def test_spare(frames):
    # If in two tries he knocks them all down, this is called a “spare”
    #  and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).
    frames[0] = (1, 9)
    frames[1] = (1, 0)
    expected_score = 12

    score = score_game(frames)

    assert expected_score == score

"""
Bowling Kata
Based upon Uncle Bob's Adeventure's in C# Bowling Game

Problem Description

Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling,
produces the total score for the game. Here are some things that the program will not do:


If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.

If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.

The game score is the total of all frame scores.

Rules Reference


"""
