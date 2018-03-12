"""
## Write a program that...

### Has an input such that
- The first line is two integers n and m, the number of lines and columns
  - **constraint:** 0 < n < m <= 100
- The next n lines contains exactly m characters and represent the field
  - Each safe square is represented by an “.” character
  - Each mine square is represented by an “*” character

### Output
- n lines with the “.” characters replaced with the number of adjacent mines
"""
from pytest import mark

from kata.mine_sweeper.mine_sweeper import MineSweeper


def test_build_solution_field():
    expected_field = '1 1\n*'

    game_input = '1 1\n*'
    mine_sweeper = MineSweeper(game_input)

    assert expected_field == mine_sweeper.field


@mark.parametrize('field_size, expected_lines', [
    ('1 1', 1),
    ('2 1', 2),
    ('3 1', 3),
    ('5 1', 5),
    ('10 1', 10),
])
def test_lines(field_size, expected_lines):
    field = '\n'.join(['*' for _ in range(expected_lines)])

    mine_sweeper = MineSweeper(f'{field_size}\n{field}')

    assert expected_lines == mine_sweeper.lines

# @mark.parametrize('field_size, expected_columns', [
#     ('1 1', 1),
#     ('1 2', 2),
#     ('1 3', 3),
#     ('1 5', 5),
#     ('1 10', 10),
# ])
# def test_columns(field_size, expected_columns):
#     field = '\n'.join(['*' for _ in range(expected_columns)])
#
#     mine_sweeper = MineSweeper(f'{field_size}\n{field}')
#
#     assert expected_columns == mine_sweeper.columns
