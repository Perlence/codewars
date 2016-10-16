"""Strings mix (4 kyu)"""

from collections import Counter
from functools import cmp_to_key


def mix(s1, s2):
    result = {}

    s1 = [l for l in s1 if l.isalpha() and l.islower()]
    s2 = [l for l in s2 if l.isalpha() and l.islower()]

    cr1 = Counter(s1)
    cr2 = Counter(s2)

    for l in set(cr1.keys() + cr2.keys()):
        c1 = cr1.get(l, 0)
        c2 = cr2.get(l, 0)
        if c1 < 2 and c2 < 2:
            continue
        if c1 > c2:
            result[l] = (c1, '1')
        elif c2 > c1:
            result[l] = (c2, '2')
        else:
            result[l] = (c1, '=')

    return '/'.join('{}:{}'.format(s, l*c)
                    for l, (c, s) in sorted(result.items(),
                                            key=cmp_to_key(mix_cmp)))


def mix_cmp(a, b):
    (l1, (c1, s1)), (l2, (c2, s2)) = a, b
    if c1 > c2:
        return -1
    elif c1 < c2:
        return 1

    if s1 > s2:
        return 1
    elif s1 < s2:
        return -1

    return cmp(l1, l2)


def test_mix():
    assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
    assert mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
    assert mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
    assert mix("codewars", "codewars") == ""
    assert mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
