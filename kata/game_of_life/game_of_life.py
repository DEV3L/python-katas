def game_of_life(input_board):
    input_board_lines = input_board.split('\n')

    generation_header = input_board_lines[0].replace('1', '2')
    board_size = input_board_lines[1]

    if '0 0' == board_size:
        output = '\n'.join([generation_header, board_size]) + '\n'
        return output

    start_state = input_board_lines[2:]
    live_cells = []
    # find life
    for x, game_row in enumerate(start_state):
        for y, cell in enumerate(game_row):
            if cell == '*':
                live_cells.append((x, y))

    board_dimensions = board_size.split(' ')
    board = [['.' for x in range(int(board_dimensions[1]))] for y in range(int(board_dimensions[0]))]

    for x, board_row in enumerate(board):
        for y, board_cell in enumerate(board_row):
            is_live = (x, y) in live_cells

            # count neighbors
            # xxx -> (x-1, y-1), (x, y-1), (x+1, y-1)
            # xox -> (x-1, y), (SELF), (x+1, y)
            # xxx -> (x-1, y+1), (x, y+1), (x+1, y+1)
            neighbor_count = 0

            # top row
            neighbor_count += is_live_cell(live_cells, x - 1, y - 1)
            neighbor_count += is_live_cell(live_cells, x, y - 1)
            neighbor_count += is_live_cell(live_cells, x + 1, y - 1)

            # middle
            neighbor_count += is_live_cell(live_cells, x - 1, y)
            # Skip SELF neighbor_count += is_live_cell(board, x, y)
            neighbor_count += is_live_cell(live_cells, x + 1, y)

            # bottom
            neighbor_count += is_live_cell(live_cells, x - 1, y + 1)
            neighbor_count += is_live_cell(live_cells, x, y + 1)
            neighbor_count += is_live_cell(live_cells, x + 1, y + 1)

            if not is_live and neighbor_count == 3:
                is_live = True
            elif is_live and (neighbor_count == 2 or neighbor_count == 3):
                is_live = True
            else:
                is_live = False

            board[x][y] = '*' if is_live else '.'

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


def is_live_cell(live_cells, x, y):
    return 1 if (x, y) in live_cells else 0
