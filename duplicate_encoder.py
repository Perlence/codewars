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
