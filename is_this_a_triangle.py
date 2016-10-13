"""Is this a triangle? (7 kyu)

Implement a method that accepts 3 integer values a, b, c. The method
should return true if a triangle can be built with the sides of given
length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be
accepted).

https://www.codewars.com/kata/is-this-a-triangle
"""


def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b


def test_is_triangle():
    assert is_triangle(1, 2, 2)
    assert not is_triangle(7, 2, 2)
    assert not is_triangle(1, 2, 3)
    assert not is_triangle(1, 3, 2)
    assert not is_triangle(3, 1, 2)
    assert not is_triangle(5, 1, 2)
    assert not is_triangle(1, 2, 5)
    assert not is_triangle(2, 5, 1)
    assert is_triangle(4, 2, 3)
    assert is_triangle(5, 1, 5)
    assert is_triangle(2, 2, 2)
    assert not is_triangle(-1, 2, 3)
    assert not is_triangle(1, -2, 3)
    assert not is_triangle(1, 2, -3)
    assert not is_triangle(0, 2, 3)
