"""Duplicate encoder (6 kyu)

The goal of this exercise is to convert a string to a new string where
each character in the new string is '(' if that character appears only
once in the original string, or ')' if that character appears more than
once in the original string. Ignore capitalization when determining if a
character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("

https://www.codewars.com/kata/duplicate-encoder
"""

import collections


def duplicate_encode(word):
    lower = word.lower()
    counts = collections.Counter(lower)
    result = ''
    for ch in lower:
        if counts[ch] == 1:
            result += '('
        else:
            result += ')'
    return result


def test_duplicate_encode():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())", "should ignore case"
    assert duplicate_encode("(( @") == "))(("
