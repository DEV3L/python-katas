from kata.game_of_life.game_of_life import game_of_life


def test_game_of_life_empty_board():
    expected_next_generation = ''

    generation_input = \
        'Generation 1:\n' \
        '0 0\n' \
        ''

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation
