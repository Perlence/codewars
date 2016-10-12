"""RGB To Hex Conversion

The rgb() method is incomplete. Complete the method so that passing in
RGB decimal values will result in a hexadecimal representation being
returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b)
argument values that fall out of that range should be rounded to the
closest valid value.

The following are examples of expected output values:

    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    return '{:02X}{:02X}{:02X}'.format(min(max(r, 0), 255),
                                       min(max(g, 0), 255),
                                       min(max(b, 0), 255))


def test_rgb():
    assert rgb(0, 0, 0) == "000000", "testing zero values"
    assert rgb(1, 2, 3) == "010203", "testing near zero values"
    assert rgb(255, 255, 255) == "FFFFFF", "testing max values"
    assert rgb(254, 253, 252) == "FEFDFC", "testing near max values"
    assert rgb(-20, 275, 125) == "00FF7D", "testing out of range values"
