
def test_bowling_class():
    from bowling import Bowling

    bowling = Bowling([])

    assert [] == bowling.frames
    assert 0 == bowling.score
