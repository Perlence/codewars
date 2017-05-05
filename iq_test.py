"""IQ Test (6 kyu)

https://www.codewars.com/kata/iq-test
"""


def iq_test(numbers):
    nums = map(int, numbers.split())
    odds = []
    evens = []
    for n in nums:
        if n % 2:
            odds.append(n)
        else:
            evens.append(n)
    if len(odds) == 1:
        return nums.index(odds[0]) + 1
    elif len(evens) == 1:
        return nums.index(evens[0]) + 1


def test_iq_test():
    assert iq_test('2 4 7 8 10') == 3
    assert iq_test('1 2 2') == 1
