from AOC.day import answer


def test_one():
    a = answer("test/inputs/input01")
    assert(a.execute() == 12)


def test_two():
    a = answer("test/inputs/input02")
    assert(a.execute_two() == 'fgij')

