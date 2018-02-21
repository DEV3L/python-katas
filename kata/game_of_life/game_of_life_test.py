from kata.game_of_life.game_of_life import game_of_life


def test_game_of_life_zero_board():
    expected_next_generation = \
        'Generation 2:\n' \
        '0 0\n' \
        ''

    generation_input = \
        'Generation 1:\n' \
        '0 0\n' \
        ''

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_one_empty_board():
    expected_next_generation = \
        'Generation 2:\n' \
        '1 1\n' \
        '.'

    generation_input = \
        'Generation 1:\n' \
        '1 1\n' \
        '.'

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_one_live_board():
    expected_next_generation = \
        'Generation 2:\n' \
        '1 1\n' \
        '.'

    generation_input = \
        'Generation 1:\n' \
        '1 1\n' \
        '*'

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation
