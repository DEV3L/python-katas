"""
# Three Laws of Test Driven Development
- You are not allowed to write any production code unless it is to make a failing unit test pass.
- You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
- You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

S - Single Responsibility Principle
O - Open / Closed => Open for extension, closed for modification
L - Liskov Substitution => shape.area :: rectangle.area : square.area : circle.area
I - Interface Segregation
D - Dependency Inversion

D - Don't
R - Repeat
Y - Yourself

Fake it till you make it

# ZOMBIES
Z - Zero
O - One
M - Many
B - Boundary Behavior
I - Interface Definition
E - Exercise Exception Behavior
S - Simple
"""
from kata.breakwall.breakwall import elf_report, elf_multiply, elf_report_three, elf_multiply_three


def test_breakwall_zero():
    expected_no_results = []

    result = elf_report([])

    assert expected_no_results == result


def test_elf_report_one():
    expected_no_results = []

    result = elf_report([1])

    assert expected_no_results == result


def test_elf_report_2020():
    expected_results = [1010, 1010]

    result = elf_report([1010, 1010])

    assert expected_results == result


def test_elf_report_2020_with_other_numbers():
    expected_results = [1010, 1010]

    result = elf_report([1010, 5, 1010])

    assert expected_results == result


def test_elf_report_multiply_result():
    expected_no_results = 1020100

    result = elf_report([1010, 5, 1010])
    multiply_result = elf_multiply(result)

    assert expected_no_results == multiply_result


# def test_elf_report_three():
#     expected_no_results = []
#
#     result = elf_report_three([0, 0])
#
#     assert expected_no_results == result


def test_elf_report_three():
    expected_results = [979, 366, 675]

    result = elf_report_three([979, 366, 675])

    assert expected_results == result


def test_elf_report_multiply_three():
    expected_results = 241861950

    result = elf_report_three([979, 366, 675])
    multiply_result = elf_multiply_three(result)

    assert expected_results == multiply_result
