from AOC.day import answer


def test_one():
    a = answer("test/inputs/input01")
    assert(a.execute() == '')

#    a = answer(None, "abc")
#    assert(a.execute() == '')


def test_two():
    a = answer("test/inputs/input02")
    assert(a.execute_two() == '')

#    a = answer(None, "abc")
#    assert(a.execute_two() == '')

