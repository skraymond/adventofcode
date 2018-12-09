from AOC.day import answer, step, invalid_do, invalid_can_do, step_factory
from nose.tools import assert_true, assert_equals, assert_false


def test_one():
    a = answer(None, ['Step A must be finished before step H can begin.',
                      'Step B must be finished before step I can begin.',
                      'Step C must be finished before step J can begin.',
                      'Step D must be finished before step K can begin.',
                      'Step E must be finished before step L can begin.',
                      'Step F must be finished before step M can begin.',
                      'Step G must be finished before step N can begin.'])
    a.generate_timed()
    a.load_up()

    assert_equals(len(a.workers), 5)
    a.load_up()
    a.load_up()
    a.load_up()
    assert_true('A' in [worker.name for worker in a.workers])
    assert_true('B' in [worker.name for worker in a.workers])
    assert_true('C' in [worker.name for worker in a.workers])
    assert_true('D' in [worker.name for worker in a.workers])
    assert_true('E' in [worker.name for worker in a.workers])
    assert_equals(len(a.workers), 5)


def test_two():
    a = answer(None, ['Step A must be finished before step H can begin.',
                      'Step B must be finished before step I can begin.',
                      'Step C must be finished before step J can begin.',
                      'Step D must be finished before step K can begin.',
                      'Step E must be finished before step L can begin.',
                      'Step F must be finished before step M can begin.',
                      'Step G must be finished before step N can begin.'])
    a.generate_timed()
    a.load_up()

    a.second_pass()
    assert_equals(len(a.workers), 5)
    for i in range(60):
        a.second_pass()
    assert_equals(len(a.workers), 4)
    char_b = a.second_pass()
    assert_equals(char_b, 'B')
    assert_equals(len(a.workers), 3)

    a.load_up()
    assert_equals(len(a.workers), 5)


def test_three():
    a = answer(None, ['Step A must be finished before step Z can begin.',
                      'Step B must be finished before step Z can begin.',
                      'Step C must be finished before step Z can begin.'], 2)

    result = a.execute_two()
    assert_equals('ABCZ', result)
    assert_equals(61+63+86, a.seconds)


def test_final():
    a = answer(None, ['Step C must be finished before step A can begin.',
                      'Step C must be finished before step F can begin.',
                      'Step A must be finished before step B can begin.',
                      'Step A must be finished before step D can begin.',
                      'Step B must be finished before step E can begin.',
                      'Step D must be finished before step E can begin.',
                      'Step F must be finished before step E can begin.'],
               2)
    results = a.execute_two()
# Change the time to 1 in the timed_steps for this to work    
#    assert_equals(a.seconds, 15)
#    assert_equals(results, 'CABFDE')

