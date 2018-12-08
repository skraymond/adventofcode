import pdb
from AOC.day import answer, space_index, high_index
from nose.tools import assert_equals, assert_true, assert_false


def test_one():
    a = answer(None, 'aA')
    assert_equals(a.next_index(0), 1)

    a = answer(None, ['a', '', 'A'])
    assert_equals(a.next_index(0), 2)

    a = answer(None, '1aA')
    assert_equals(a.next_index(0), 1)

    a = answer(None, '1aA')
    assert_equals(a.next_index(1), 2)

    a = answer(None, ['1', 'a', '', 'A'])
    assert_equals(a.next_index(1), 3)

    try: 
        a = answer(None, ['1', 'a', '', 'A'])
        a.next_index(2)
        assert_true(False)
    except space_index:
        pass
        
    a = answer(None, ['1', 'a', '', ''])
    assert_equals(a.next_index(1), None)

    a = answer(None, [])
    assert_equals(a.next_index(0), None)

def test_one_b():
    a = answer(None, 'aA')
    assert_equals(a.rev_index(0), 0)

    a = answer(None, ['a', '', 'A'])
    assert_equals(a.rev_index(0), 0)

    a = answer(None, ['a', '', 'A'])
    assert_equals(a.rev_index(1), 0)

    a = answer(None, '1aA')
    assert_equals(a.rev_index(1), 1)

    a = answer(None, '1aA')
    assert_equals(a.rev_index(2), 2)

    a = answer(None, ['1', 'a', '', 'A'])
    assert_equals(a.rev_index(2), 1)

    a = answer(None, ['1', 'a', '', ''])
    assert_equals(a.rev_index(3), 1)

    a = answer(None, ['', '', '', ''])
    assert_equals(a.rev_index(3), None)


    a = answer(None, ['', ''])
    assert_equals(a.rev_index(1), None)

    a = answer(None, ['1', '', '', '1'])
    assert_equals(a.rev_index(1), 0)


def test_two():
    a = answer(None, 'aA')
    assert_true(a.chars_match(0, 1))

    a = answer(None, 'Aa')
    assert_true(a.chars_match(0, 1))

    a = answer(None, 'A a')
    assert_true(a.chars_match(0, 2))

    a = answer(None, 'a A')
    assert_true(a.chars_match(0, 2))

    a = answer(None, 'AA')
    assert_false(a.chars_match(0, 1))

    a = answer(None, 'aa')
    assert_false(a.chars_match(0, 1))

    try:
        a = answer(None, ['a', ''])
        a.chars_match(0, 1)
        assert_true(False)
    except:
        pass

    try:
        a = answer(None, ['','a'])
        a.chars_match(0, 1)
        assert_true(False)
    except:
        pass

def test_three():
    a = answer(None, 'aA')
    assert_equals(a.reduce_data(), '')

    a = answer(None, 'Aa')
    assert_equals(a.reduce_data(), '')

    a = answer(None, 'abBA')
    assert_equals(a.reduce_data(), '')

    a = answer(None, 'abAB')
    assert_equals(a.reduce_data(), 'abAB')

    a = answer(None, 'aabAAB')
    assert_equals(a.reduce_data(), 'aabAAB')

    a = answer(None, '1aA')
    assert_equals(a.reduce_data(), '1')

    a = answer(None, 'aA1')
    assert_equals(a.reduce_data(), '1')


    a = answer(None, '1aA1bBBbBb')
    assert_equals(a.reduce_data(), '11')

    a = answer(None, '1aA1')
    assert_equals(a.reduce_data(), '11')

    a = answer(None, 'bBBbBb1aA1')
    assert_equals(a.reduce_data(), '11')

def test_four():
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.reduce_data(), 'dabCBAcaDA')


def five():
    a = answer(None, "1" + str("Aa" * 50001))
    assert_equals(a.reduce_data(), '1')

    a = answer(None, str("Aa" * 50001) + "1")
    assert_equals(a.reduce_data(), '1')

    a = answer(None, str("1Aa" * 50001))
    assert_equals(a.reduce_data(), '1' * 50001)

    
def test_six():
    inp = str("A" * 5000) + str('bB') + str("a" * 5000)
    assert_equals(answer(None, inp).reduce_data(), '')

    
def test_seven():
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.execute(), 10)
    

def test_eight():
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.remove_one('A'), 6)    
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.remove_one('B'), 8)
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.remove_one('C'), 4)
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.remove_one('D'), 6)

def test_nine():
    a = answer(None, "dabAcCaCBAcCcaDA")
    assert_equals(a.execute_two(), 4)    
