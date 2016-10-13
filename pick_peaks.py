"""Pick peaks (4 kyu)

In this kata, you will create an object that returns the positions and
the values of the "peaks" (or local maxima) of a numeric array.

For example,  the array `arr = [ 0 , 1 , 2 , 5 , 1 , 0 ]` has a peak in
position 3 with a value of 5 (arr[3] = 5)

The output will be returned as an object with two properties: pos and
peaks.  Both of these properties should be arrays. If there is no peak
in the given array, then the output should be `{pos: [], peaks: []}`.

Example: `pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])` returns
`{pos:[3,7],peaks:[6,3]}`

All input arrays  will be valid numeric arrays (although it could still
be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks
(in the context of a mathematical function, we don't know what is after
and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! `[1,2,2,2,1]` has a peak while `[1, 2, 2,
2, 3]` does not. In case of a plateau-peak, please only return the
position and value of the beginning of the plateau. For example:
`pick_peaks([1,2,2,2,1])` returns `{pos:[1],peaks:[2]}`

have fun!

https://www.codewars.com/kata/pick-peaks
"""


def pick_peaks(seq):
    pos = []
    peaks = []
    b = 0

    for i, (a, b) in enumerate(pairwise(diff(seq)), start=1):
        if a > 0 and b <= 0:
            pos.append(i)
            peaks.append(seq[i])

    if b == 0 and pos and peaks:
        pos.pop()
        peaks.pop()

    return {'pos': pos, 'peaks': peaks}


def diff(iterable):
    for a, b in pairwise(iterable):
        yield b - a


def pairwise(iterable):
    it = iter(iterable)
    prev = next(it)
    for cur in it:
        yield prev, cur
        prev = cur


def test_pick_peaks():
    assert pick_peaks([]) == {'pos': [], 'peaks': []}, \
        'should support empty lists'

    assert pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]) == {'pos': [3, 7], 'peaks': [6, 3]}, \
        'should support finding peaks'

    assert pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) == {'pos': [3, 7], 'peaks': [6, 3]}, \
        'should support finding peaks, but should ignore peaks on the edge of the array'

    assert pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]) == {'pos': [3, 7, 10], 'peaks': [6, 3, 2]}, \
        'should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau'

    assert pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]) == {'pos': [2, 4], 'peaks': [3, 2]}, \
        'should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau'

    assert pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]) == {'pos': [2], 'peaks': [3]}, \
        'should support finding peaks, but should ignore peaks on the edge of the array'
    assert pick_peaks([2, 2, 1, 3, 1, 2, 2, 2, 2]) == {'pos': [3], 'peaks': [3]}, \
        'should support finding peaks, but should ignore peaks on the edge of the array'

    assert pick_peaks([1, 2, 2, 2, 3]) == {'pos': [], 'peaks': []}, \
        'should ignore sorted sequences'
    assert pick_peaks([3, 2, 2, 2, 1]) == {'pos': [], 'peaks': []}, \
        'should ignore sorted sequences'
