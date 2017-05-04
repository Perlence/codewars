"""Number of Proper Fractions with Denominator d (4 kyu)

https://www.codewars.com/kata/55b7bb74a0256d4467000070
"""

from fractions import gcd
from itertools import groupby

try:
    profile
except NameError:
    def profile(func):
        return func


def proper_fractions_naive(n):
    result = 0
    for m in xrange(1, n):
        if gcd(m, n) == 1:
            result += 1
    return result


def proper_fractions_sieve(n):
    sieve = set()
    divs = set(divisors(n))
    for m in xrange(2, n):
        if m in sieve or m not in divs:
            continue
        for k in xrange(1, int(n/m)):
            sieve.add(m*k)
    return n - len(sieve) - 1


@profile
def proper_fractions_factored(n):
    if n == 1:
        return 0
    primes = groupby(factors(n))
    result = 1
    for p, grouper in primes:
        a = ilen(grouper)
        result *= (p-1) * p**(a-1)
    return result


def divisors(n):
    result = set()
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            result.update([i, n//i])
    return result


@profile
def factors(n):
    while n > 1:
        for i in xrange(2, n + 1):
            if n % i == 0:
                n /= i
                yield i
                break


def ilen(it):
    return sum(1 for _ in it)


# proper_fractions = proper_fractions_naive
# proper_fractions = proper_fractions_sieve
proper_fractions = proper_fractions_factored


def test_proper_fractions():
    assert proper_fractions(1) == 0
    assert proper_fractions(2) == 1
    assert proper_fractions(5) == 4
    assert proper_fractions(15) == 8
    assert proper_fractions(16) == 8
    assert proper_fractions(25) == 20
    assert proper_fractions(1000000) == 400000
    assert proper_fractions(10000000) == 4000000
    assert proper_fractions(20000000) == 8000000
    assert proper_fractions(50000000) == 20000000
    # assert proper_fractions(90000003) == 60000000


if __name__ == '__main__':
    import sys
    import pytest
    pytest.main(sys.argv)
