# Parse String Time

A time conversion problem...


### Difficulty
*low?*


## Problem Description

Execution times for a program are outputted in a non-standard parseable
time format.

The format is such:
- `f'{amount} {duration type}'`
- amount is a positive integer value
- duration type is an enumeration of weighted values
  - ms  : .001
  - sec : 1
  - min : 60
  - hr  : 3600
- different duration types are joined together with a space character
- invalid input values equal zero

Create a program, which, given a valid time format, calculate the
time in seconds

|input value | expected result |
|------------|-----------------|
|'1 ms'  | .001 |
|'1 sec' | 1 |
|'1 min' | 60 |
|'1 hr'  | 3600 |
|'5 sec 421 ms' | 5.421 |
|'9 min 57 sec' | 597 |
|'1 hr 33 min'  | 5580 |
|'1 hr 1 min 1 sec 111 ms' | 3661.111 |
|'' | 0 |
