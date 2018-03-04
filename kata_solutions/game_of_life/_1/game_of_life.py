class Game:
    DEAD_CELL = '.'
    LIVE_CELL = '*'

    def __init__(self, input_game_data):
        self._input_game_data_lines = input_game_data.split('\n')
        self._live_cells = None

    @property
    def next_generation_header(self):
        return self._input_game_data_lines[0].replace('1', '2')

    @property
    def board_size(self):
        return self._input_game_data_lines[1]

    @property
    def start_state(self):
        return self._input_game_data_lines[2:]

    def find_live_cells(self):
        if self._live_cells:
            return self._live_cells

        self._live_cells = []
        for x, game_row in enumerate(self.start_state):
            for y, cell in enumerate(game_row):
                if cell == self.LIVE_CELL:
                    self._live_cells.append((x, y))

        return self._live_cells

    def build_empty_board(self):
        board_dimensions = self.board_size.split(' ')
        empty_board = [[self.DEAD_CELL for x in range(int(board_dimensions[1]))] for y in
                       range(int(board_dimensions[0]))]
        return empty_board


def game_of_life(input_board):
    game = Game(input_board)

    live_cells = game.find_live_cells()
    board = game.build_empty_board()

    for x, board_row in enumerate(board):
        for y, board_cell in enumerate(board_row):
            is_live = (x, y) in live_cells

            neighbor_count = _count_neighbors(live_cells, x, y)

            if not is_live and neighbor_count == 3:
                is_live = True
            elif is_live and (neighbor_count == 2 or neighbor_count == 3):
                is_live = True
            else:
                is_live = False

            board[x][y] = '*' if is_live else '.'

    output = [game.next_generation_header, game.board_size]

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


def _count_neighbors(live_cells, x, y):
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

    return neighbor_count


def is_live_cell(live_cells, x, y):
    return 1 if (x, y) in live_cells else 0
