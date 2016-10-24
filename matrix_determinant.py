"""Matrix Determinant (4 kyu)

https://www.codewars.com/kata/matrix-determinant
"""

from __future__ import print_function


def determinant(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return sum(((-1) ** j) * v * determinant(minor(m, 0, j))
               for j, v in enumerate(m[0]))


def minor(m, x, y):
    return [[v for j, v in enumerate(row) if j != y]
            for i, row in enumerate(m) if i != x]


def test_minor():
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    assert minor(m1, 0, 0) == [[5, 6], [8, 9]]
    assert minor(m1, 0, 1) == [[4, 6], [7, 9]]
    assert minor(m1, 0, 2) == [[4, 5], [7, 8]]


def test_determinant():
    m1 = [[1, 3],
          [2, 5]]
    m2 = [[2, 5, 3],
          [1, -2, -1],
          [1, 3, 4]]

    assert determinant([[1]]) == 1
    assert determinant(m1) == -1
    assert determinant(m2) == -20
