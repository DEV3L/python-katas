from kata_solutions.game_of_life._1.game_of_life import game_of_life


def test_game_of_life_zero_board():
    expected_next_generation = _build_board(2, (0, 0), ())
    generation_input = _build_board(1, (0, 0), ())

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_one_empty_board():
    expected_next_generation = _build_board(2, (1, 1), ())
    generation_input = _build_board(1, (1, 1), ())

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_one_live_board():
    expected_next_generation = _build_board(2, (1, 1), ())
    generation_input = _build_board(1, (1, 1), ((0, 0),))

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_fewer_than_two_neighbors():
    expected_next_generation = _build_board(2, (2, 2), ())
    generation_input = _build_board(1, (2, 2), ((0, 0), (1, 1)))

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_dead_cell_three_neighbors_lives():
    # ** -> **
    # .* -> **
    expected_next_generation = _build_board(2, (2, 2), ((0, 0), (0, 1), (1, 0), (1, 1)))
    generation_input = _build_board(1, (2, 2), ((0, 0), (0, 1), (1, 1)))

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def test_game_of_life_example_board():
    expected_next_generation = '''Generation 2:
4 8
........
...**...
...**...
........'''

    generation_input = '''Generation 1:
4 8
........
....*...
...**...
........'''

    next_generation = game_of_life(generation_input)

    assert expected_next_generation == next_generation


def _build_board(generation: int, board_size: tuple, live_nodes: tuple):
    return_generation = f'Generation {generation}:\n'
    return_generation += f'{board_size[0]} {board_size[1]}\n'

    board = [['.' for x in range(board_size[0])] for y in range(board_size[1])]

    for node in live_nodes:
        board[node[0]][node[1]] = '*'

    board_str = ''

    for row in board:
        row_str = ''
        for cell in row:
            row_str += cell
        board_str += row_str + '\n'

    board_str = board_str.rstrip('\n')

    return_generation += board_str

    return return_generation
