# Mine Sweeper

### Difficulty
*Easy*

## Problem Description

[Original Problem Description](acm.uva.es/p/v101/10189.html)

The goal in a game of Mine Sweeper is to find all the mines within an MxN field.

To help you, the game shows a number in a square which tells you how many mines there are adjacent to that square.

For instance, take the following 4x4 field with 2 mines (which are represented by an * character):
```
*...
....
.*..
....
```

The same field including the hint numbers described above would look like this:

```
*100
2210
1*10
1110
```

---

Write a program that takes input as follows:

The first line of each field contains two integers n and m
(0 < n,m <= 100) which stands for the number of lines and columns of
the field respectively.

The next n lines contains exactly m characters and represent the field.

Each safe square is represented by an “.” character.

Each mine square is represented by an “*” character.

The first field line where n = m = 0 represents the end of input and
should not be processed.

Your program should produce output as follows:

For each field, you must print the following message in a line alone:

Field #x:

Where x stands for the number of the field (starting from 1).

The next n lines should contain the field with the “.” characters
replaced by the number of adjacent mines to that square.

There must be an empty line between field outputs.

#### Clues

As you may have already noticed, each square may have at most 8 adjacent squares.

## Test Cases
**Input**
Mine Field #1:
```
4 4
*...
....
.*..
....
```

Mine Field #2:
```
3 5
**...
.....
.*...
0 0
```

**Expected**
Mine Field #1:
```
*100
2210
1*10
1110
```

Mine Field #2:
```
**100
33200
1*100
```
