"""Vasya - Clerk (6 kyu)

https://www.codewars.com/kata/vasya-clerk
"""


def tickets(people):
    cash = []
    for bill in people:
        cash.append(bill)
        try:
            if bill == 50:
                cash.remove(25)
            elif bill == 100:
                cash.remove(25)
                try:
                    cash.remove(50)
                except ValueError:
                    cash.remove(25)
                    cash.remove(25)
        except ValueError:
            return 'NO'
    return 'YES'


def test_tickets():
    assert tickets([25, 25, 50]) == 'YES'
    assert tickets([25, 100]) == 'NO'
    assert tickets([25, 25, 25, 100]) == 'YES'
