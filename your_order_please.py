"""Your order, please (6 kyu)

Your task is to sort a given string. Each word in the String will
contain a single number. This number is the position the word should
have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the
input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2
3a T4est"

https://www.codewars.com/kata/your-order-please
"""


def order(sentence):
    return ' '.join(sorted(sentence.split(), key=key))


def key(s):
    return int(''.join(c for c in s if c.isdigit()))


def test_key():
    assert key('Thi1s') == 1
    assert key('is2') == 2
    assert key('3a') == 3
    assert key('T4est') == 4


def test_order():
    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
