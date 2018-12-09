from AOC.day import answer, step, invalid_do, invalid_can_do, timed_step
from nose.tools import assert_true, assert_equals, assert_false, assert_equal


def test_timed_one():
    s1 = timed_step('A')
    assert_false(s1.isDone())
    assert_equal(s1._time, 61)

    s1.do()
    assert_false(s1.isDone())
    assert_equal(s1._time, 60)

    for i in range(60):
        s1.do()
    assert_true(s1.isDone())


def test_steps_one():
    s1 = step('A')
    assert_false(s1.isDone())
    s1.do()
    assert_true(s1.isDone())


def test_steps_two():
    s1 = step('A')    
    s2 = step('B')
    s1.add_preq(s2)

    assert_false(s1.can_do())
    assert_false(s1.isDone())
    assert_false(s2.isDone())

    s2.do()
    assert_true(s1.can_do())
    assert_false(s1.isDone())
    assert_true(s2.isDone())

    s1.do()    
    assert_true(s1.isDone())


def test_steps_four():
    s1 = step('A')
    s1.add_preq(step('B'))
    try:
        s1.do()
        assert_true(False)
    except invalid_do:
        pass


    s1 = step('A')
    s1.do()
    try:
        s1.can_do()
        assert_true(False)
    except invalid_can_do:
        pass


def test_steps_three():
    s1 = step('A')    
    s2a = step('Ba')
    s2b = step('Bb')
    s2c = step('Bc')
    for s2 in [s2a, s2b, s2c]:
        s1.add_preq(s2)

    assert_false(s1.isDone())
    for s2 in [s2a, s2b, s2c]:
        assert_false(s2.isDone())

    s2a.do()
    assert_false(s1.isDone())
    assert_false(s1.can_do())
    assert_true(s2a.isDone())
    for s2 in [s2b, s2c]:
        assert_false(s2.isDone())

    s2b.do()
    s2c.do()
    assert_false(s1.isDone())
    assert_true(s1.can_do())


def test_steps_five():
    s1 = step('A')    
    s2 = step('B')
    s3 = step('C')
    s1.add_preq(s2)
    s2.add_preq(s3)

    assert_false(s1.can_do())
    assert_false(s1.isDone())
    assert_false(s2.can_do())
    assert_true(s3.can_do())

    s3.do()
    assert_false(s1.can_do())
    assert_false(s1.isDone())
    assert_true(s2.can_do())

    s2.do()
    assert_true(s1.can_do())
    assert_false(s1.isDone())

    s1.do()
    assert_true(s1.isDone())


