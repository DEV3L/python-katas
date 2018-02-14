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
    (30, list(itertools.repeat((1, 2), 10))),
    # spares
    (12, [(1, 9), (1, 0)]),
    (30, [(1, 9), (10, 0)]),
    (36, [(1, 9), (2, 8), (7, 0)]),
    # strikes
    (12, [(10, 0), (1, 0)]),
    (14, [(10, 0), (1, 1)]),
    (33, [(10, 0), (10, 0), (1, 0)]),
    (60, [(10, 0), (10, 0), (10, 0)]),
    # tenth frame
    (10, list(itertools.repeat((0, 0), 9)) + [(9, 1, 0)]),
    (11, list(itertools.repeat((0, 0), 9)) + [(9, 1, 1)]),
    (10, list(itertools.repeat((0, 0), 9)) + [(10, 0, 0)]),
    (11, list(itertools.repeat((0, 0), 9)) + [(10, 1, 0)]),
    (21, list(itertools.repeat((0, 0), 9)) + [(10, 10, 1)]),
    # all strikes
    (300, list(itertools.repeat((10, 0), 9)) + [(10, 10, 10)]),
])
def test_score(expected_score, scores, frames):
    _substitute_frame_scores(frames, scores)

    score = score_game(frames)
    assert expected_score == score


def _substitute_frame_scores(frames, scores):
    for index, score in enumerate(scores):
        frames[index] = score
