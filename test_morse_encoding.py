from morse_encoding import Morse


def test_morse():
    assert Morse.encode('HELLO WORLD') == [-1440552402, -1547992901, -1896993141, -1461059584]
    assert Morse.decode([-1440552402, -1547992901, - 1896993141, -1461059584]) == 'HELLO WORLD'
    assert Morse.encode('EEEEEEEIE') == [-2004318070, 536870912]
    assert Morse.decode([-2004318070, 536870912]) == 'EEEEEEEIE'
