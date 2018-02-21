import itertools

from kata.game_of_life.game_of_life import game_of_life


def test_game_of_life_zero_board():
    expected_next_generation = _build_board(2, (0, 0), ())
    generation_input = _build_board(1, (1, 1), ())

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_one_empty_board():
    expected_next_generation = _build_board(2, (1, 1), ())
    generation_input = _build_board(1, (1, 1), ())

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_one_live_board():
    expected_next_generation = _build_board(2, (1, 1), ())
    generation_input = \
        'Generation 1:\n' \
        '1 1\n' \
        '*'

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def _build_board(generation_number: int, board_size: tuple, live_nodes: tuple):
    return_generation = f'Generation {generation_number}:\n'
    return_generation += f'{board_size[0]} {board_size[1]}\n'

    board_line = ''.join(list(itertools.repeat('.', board_size[0])))
    board = '\n'.join(list(itertools.repeat(board_line, board_size[1])))

    return_generation += board

    return return_generation
