from AOC.day import answer, step, invalid_do, invalid_can_do, step_factory
from nose.tools import assert_true, assert_equals, assert_false


def test_parser_one():
    factory = step_factory()
    factory.parse('Step A must be finished before step C can begin.')
    
    steps = factory.get_steps()
    
    s1 = steps['C']
    s2 = steps['A']

    assert_false(s1.can_do())
    assert_true(s2.can_do())
    assert_false(s1.isDone())
    assert_false(s2.isDone())
    
    s2.do()
    assert_true(s1.can_do())

    s1.do()
    assert_true(s1.isDone())


def test_time_parser_one():
    factory = step_factory()
    factory.parse_timed('Step A must be finished before step C can begin.')
    
    steps = factory.get_steps()
    
    s1 = steps['C']
    s2 = steps['A']

    assert_false(s1.can_do())
    assert_true(s2.can_do())
    assert_false(s1.isDone())
    assert_false(s2.isDone())

    for i in range(61):
        s2.do()
    assert_true(s1.can_do())

    for i in range(63):
        s1.do()
    assert_true(s1.isDone())


def test_one():
    a = answer(None, ['Step A must be finished before step C can begin.'])
    a.generate()
    
    assert_equals(len(a.steps), 2)
    assert_true('A' in a.steps)
    assert_true('C' in a.steps)


def test_one_timed():
    a = answer(None, ['Step A must be finished before step C can begin.'])
    a.generate()
    
    assert_equals(len(a.steps), 2)
    assert_true('A' in a.steps)
    assert_true('C' in a.steps)


def test_two():
    a = answer(None, ['Step A must be finished before step C can begin.'])
    a.generate()
    a.run_a_step()
    
    assert_true(a.steps['A'].isDone())
    assert_true(a.steps['C'].can_do())
    assert_false(a.steps['C'].isDone())

    a.run_a_step()
    assert_true(a.steps['C'].isDone())
    

def test_three():
    a = answer(None, ['Step C must be finished before step A can begin.'])
    assert_equals(a.execute(), 'CA')


def test_final():
    a = answer(None, ['Step C must be finished before step A can begin.',
                      'Step C must be finished before step F can begin.',
                      'Step A must be finished before step B can begin.',
                      'Step A must be finished before step D can begin.',
                      'Step B must be finished before step E can begin.',
                      'Step D must be finished before step E can begin.',
                      'Step F must be finished before step E can begin.'])
    assert(a.execute() == 'CABDFE')


def test_final_two():
    a = answer(None, ['Step F must be finished before step E can begin.',
                      'Step A must be finished before step B can begin.',
                      'Step B must be finished before step E can begin.',
                      'Step C must be finished before step F can begin.',
                      'Step A must be finished before step D can begin.',
                      'Step D must be finished before step E can begin.',
                      'Step C must be finished before step A can begin.'])
    assert(a.execute() == 'CABDFE')


def test_final_three():
    a = answer(None, ['Step Z must be finished before step A can begin.',
                      'Step Z must be finished before step F can begin.',
                      'Step A must be finished before step B can begin.',
                      'Step A must be finished before step D can begin.',
                      'Step B must be finished before step E can begin.',
                      'Step D must be finished before step E can begin.',
                      'Step F must be finished before step E can begin.'])
    assert_equals(a.execute(), 'ZABDFE')




