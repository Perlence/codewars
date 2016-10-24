"""Morse Encoding (3 kyu)

https://www.codewars.com/kata/morse-encoding
"""

from itertools import zip_longest


class Morse:
    @classmethod
    def encode(self, message):
        bi = '0000000'.join(['000'.join(self.alpha[char] for char in word)
                             for word in message.split()])
        return [to_signed_32(int(''.join(group), 2))
                for group in grouper(bi, 32, '0')]

    @classmethod
    def decode(self, seq):
        pass

    alpha = {
        'A': '10111',
        'B': '111010101',
        'C': '11101011101',
        'D': '1110101',
        'E': '1',
        'F': '101011101',
        'G': '111011101',
        'H': '1010101',
        'I': '101',
        'J': '1011101110111',
        'K': '111010111',
        'L': '101110101',
        'M': '1110111',
        'N': '11101',
        'O': '11101110111',
        'P': '10111011101',
        'Q': '1110111010111',
        'R': '1011101',
        'S': '10101',
        'T': '111',
        'U': '1010111',
        'V': '101010111',
        'W': '101110111',
        'X': '11101010111',
        'Y': '1110101110111',
        'Z': '11101110101',
        '0': '1110111011101110111',
        '1': '10111011101110111',
        '2': '101011101110111',
        '3': '1010101110111',
        '4': '10101010111',
        '5': '101010101',
        '6': '11101010101',
        '7': '1110111010101',
        '8': '111011101110101',
        '9': '11101110111011101',
        '.': '10111010111010111',
        ',': '1110111010101110111',
        '?': '101011101110101',
        "'": '1011101110111011101',
        '!': '1110101110101110111',
        '/': '1110101011101',
        '(': '111010111011101',
        ')': '1110101110111010111',
        '&': '10111010101',
        ':': '11101110111010101',
        ';': '11101011101011101',
        '=': '1110101010111',
        '+': '1011101011101',
        '-': '111010101010111',
        '_': '10101110111010111',
        '"': '101110101011101',
        '$': '10101011101010111',
        '@': '10111011101011101',
        ' ': '0'
    }


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def to_signed_32(x):
    if x <= 0x7fffffff:
        return x
    return x - 0x100000000


def test_morse():
    assert Morse.encode('HELLO WORLD') == [-1440552402, -1547992901, -1896993141, -1461059584]
    # assert Morse.decode([-1440552402, -1547992901, - 1896993141, -1461059584]) == 'HELLO WORLD'
    assert Morse.encode('EEEEEEEIE') == [-2004318070, 536870912]
    # assert Morse.decode([-2004318070, 536870912]) == 'EEEEEEEIE'
