def game_of_life(input_board):
    input_board_lines = input_board.split('\n')

    generation_header = input_board_lines[0].replace('1', '2')
    board_size = input_board_lines[1]
    board = input_board_lines[2:]

    if board_size != '0 0':
        for index, row in enumerate(board):
            board[index] = '.'

    output = [generation_header, board_size]
    output.extend(board)

    return '\n'.join(output)
