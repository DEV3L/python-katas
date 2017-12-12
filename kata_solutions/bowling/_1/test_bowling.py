from kata_solutions.bowling._1.bowling import Bowling

game_with_score_zero = [(0, 0) * 10]


def test_bowling_class():
    bowling = Bowling(game_with_score_zero)

    assert game_with_score_zero == bowling.frames


def test_score_game_score_zero():
    expected_game_score_zero = 0

    bowling = Bowling(game_with_score_zero)

    assert expected_game_score_zero == bowling.score_game()


def test_score_game_one():
    game_with_score_one = [(1, 0)]
    game_with_score_one += [(0, 0) * 9]

    expected_game_score_one = 1

    bowling = Bowling(game_with_score_one)

    assert expected_game_score_one == bowling.score_game()
