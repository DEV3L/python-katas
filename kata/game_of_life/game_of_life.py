def game_of_life(input_board):
    input_board_lines = input_board.split('\n')

    generation_header = input_board_lines[0].replace('1', '2')
    board_size = input_board_lines[1]

    if '0 0' == board_size:
        output = '\n'.join([generation_header, board_size]) + '\n'
        return output

    # start_state = input_board_lines[2:]
    # live_cells = []
    # # find life
    # for x, game_row in enumerate(start_state):
    #     for y, cell in enumerate(game_row):
    #         live_cells.append((x,y))

    board_dimensions = board_size.split(' ')
    board = [['.' for x in range(int(board_dimensions[0]))] for y in range(int(board_dimensions[1]))]

    # for index, row in enumerate(board):
    #     board[index] = '.'

    output = [generation_header, board_size]

    # for row in board:
    board_str = ''
    for row in board:
        row_str = ''
        for cell in row:
            row_str += cell
        board_str += row_str + '\n'

    board_str = board_str.rstrip('\n')
    output.append(board_str)

    return '\n'.join(output)
