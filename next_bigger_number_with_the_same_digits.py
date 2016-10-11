"""Next bigger number with the same digits

You have to create a function that takes a positive integer number and
returns the next bigger number formed by the same digits:

    next_bigger(12)==21
    next_bigger(513)==531
    next_bigger(2017)==2071

If no bigger number can be composed using those digits, return -1:

    next_bigger(9)==-1
    next_bigger(111)==-1
    next_bigger(531)==-1
"""
from itertools import permutations

NOTSET = object()


def next_bigger_perm(n):
    digs = digits(n)
    return undigit(mindef((perm for perm in permutations(digs) if perm > digs),
                          default=[-1]))


def next_bigger(num):
    digs = sorted(digits(num), reverse=True)
    maxdigs = undigit(digs)
    dr = digital_root(num)
    for n in range(num + 1, maxdigs + 1):
        if digital_root(n) == dr and sorted(digits(n), reverse=True) == digs:
            return n
    return -1


def digital_root(n):
    return (n - 1) % 9 + 1


def digits(n):
    result = ()
    while n > 9:
        n, m = divmod(n, 10)
        result = (m,) + result
    result = (n,) + result
    return result


def undigit(ns):
    result = 0
    for i, n in enumerate(reversed(ns)):
        result += n * 10 ** i
    return result


def mindef(*args, **kwargs):
    default = kwargs.pop('default', NOTSET)
    try:
        return min(*args, **kwargs)
    except ValueError:
        if default is NOTSET:
            raise
        return default


def test_mindef():
    assert mindef([1, 2, 3]) == 1
    assert mindef(1, 2, 3) == 1
    assert mindef([], default=4) == 4


def test_digits():
    assert digits(12) == (1, 2)
    assert digits(513) == (5, 1, 3)
    assert digits(2017) == (2, 0, 1, 7)
    assert digits(414) == (4, 1, 4)
    assert digits(144) == (1, 4, 4)


def test_undigit():
    assert undigit([1, 2]) == 12
    assert undigit([5, 1, 3]) == 513
    assert undigit([2, 0, 1, 7]) == 2017
    assert undigit([4, 1, 4]) == 414
    assert undigit([1, 4, 4]) == 144


def test_next_bigger():
    assert next_bigger(12) == 21
    assert next_bigger(513) == 531
    assert next_bigger(2017) == 2071
    assert next_bigger(414) == 441
    assert next_bigger(144) == 414

    assert next_bigger(9) == -1
    assert next_bigger(11) == -1
    assert next_bigger(531) == -1

    assert next_bigger(1999999999999999999999) == 9199999999999999999999
