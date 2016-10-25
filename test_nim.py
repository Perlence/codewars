from nim import *  # noqa


def test_ai_1_1():
    assert choose_move([1]) == (0, 1)
    assert choose_move([2]) == (0, 2)
    assert choose_move([3]) == (0, 3)
    assert choose_move([9]) == (0, 9)


def test_ai_2_1():
    assert choose_move([0, 1]) == (1, 1)
    assert choose_move([1, 1]) in [(0, 1), (1, 1)]  # give up
    # assert should_give_up([1, 1])
    assert choose_move([1, 2]) == (1, 1)
    assert choose_move([1, 3]) == (1, 2)
    assert choose_move([1, 9]) == (1, 8)


def test_ai_2_2():
    assert choose_move([0, 2]) == (1, 2)
    assert choose_move([2, 2]) in [(1, 1), (1, 2), (0, 1), (0, 2)]  # give up
    # assert should_give_up([2, 2])
    assert choose_move([2, 3]) == (1, 1)
    assert choose_move([2, 9]) == (1, 7)
    assert choose_move([9, 2]) == (0, 7)


def test_ai_2_3():
    # assert should_give_up([3, 3])
    assert choose_move([3, 4]) == (1, 1)
    assert choose_move([3, 9]) == (1, 6)
    assert choose_move([9, 3]) == (0, 6)


def test_ai_3_1():
    assert choose_move([1, 1, 1]) in [(0, 1), (1, 1), (2, 1)]
    assert choose_move([1, 1, 2]) == (2, 2)
    assert choose_move([1, 2, 1]) == (1, 2)
    assert choose_move([1, 1, 9]) == (2, 9)

    assert choose_move([1, 2, 2]) == (0, 1)
    # assert should_give_up([1, 2, 3])
    assert choose_move([1, 2, 4]) == (2, 1)
    assert choose_move([1, 2, 9]) == (2, 6)

    assert choose_move([1, 3, 3]) in [(0, 1), (1, 1), (2, 1)]
    assert choose_move([1, 3, 4]) == (2, 2)
    assert choose_move([1, 3, 9]) == (2, 7)

    assert choose_move([1, 4, 4]) == (0, 1)
    # assert should_give_up([1, 4, 5])
    assert choose_move([1, 4, 6]) == (2, 1)
    assert choose_move([1, 4, 9]) == (2, 4)

    assert choose_move([1, 5, 5]) in [(0, 1), (1, 1), (2, 1)]
    assert choose_move([1, 5, 6]) == (2, 2)
    assert choose_move([1, 5, 9]) == (2, 5)

    assert choose_move([1, 6, 6]) == (0, 1)
    # assert should_give_up([1, 6, 7])


def test_ai_3_2():
    assert choose_move([2, 2, 2]) in [(0, 2), (1, 2), (2, 2)]
    assert choose_move([2, 2, 3]) in [(0, 1), (1, 1), (2, 3)]
    assert choose_move([2, 2, 4]) == (2, 4)

    assert choose_move([2, 3, 3]) in [(0, 2), (1, 2), (2, 2)]
    assert choose_move([2, 3, 4]) == (2, 3)
    assert choose_move([2, 3, 9]) == (2, 8)

    assert choose_move([2, 4, 4]) == (0, 2)
    assert choose_move([2, 4, 5]) == (0, 1)
    # assert should_give_up([2, 4, 6])
    assert choose_move([2, 4, 9]) == (2, 3)

    assert choose_move([2, 5, 5]) == (0, 2)
    assert choose_move([2, 5, 6]) == (1, 1)
    # assert should_give_up([2, 5, 7])
    assert choose_move([2, 5, 8]) == (2, 1)
    assert choose_move([2, 5, 9]) == (2, 2)

    assert choose_move([2, 6, 6]) in [(0, 2), (1, 2), (2, 2)]
    assert choose_move([2, 6, 7]) in [(0, 1), (2, 3)]
    assert choose_move([2, 6, 8]) == (2, 4)
    assert choose_move([2, 6, 9]) == (2, 5)

    assert choose_move([2, 7, 7]) in [(0, 2), (1, 2), (2, 2)]
    assert choose_move([2, 7, 8]) == (2, 3)
    assert choose_move([2, 7, 9]) == (2, 4)
    assert choose_move([2, 7, 10]) == (2, 5)

    assert choose_move([2, 8, 8]) == (0, 2)
