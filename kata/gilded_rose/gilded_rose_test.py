from kata.gilded_rose.gilded_rose import GildedRose

"""
Z - Zero
O - One
M - Many
B - Boundary Behaviors
I - Interface Definition
E - Exercise Exceptional
S - Simple Scenarios, Simple Solutions
"""

"""
TDD : Test Driven Development

1. You are not allowed to write any production code unless it is to make 
    a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail; 
    and compilation failures are failures.
3. You are not allowed to write any more production code than is sufficient to pass 
    the one failing unit test.
"""


def test_zero():
    gilded_rose = GildedRose.update_quality([])

    assert len(gilded_rose) == 0
    assert gilded_rose is not None
