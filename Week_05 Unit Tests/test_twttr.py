from twttr import shorten


def test_upercase():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"


def test_lowecase():
    assert shorten("hello, world") == "hll, wrld"


def test_numeric():
    assert shorten("-2012") == "-2012"


def test_alphanumeric():
    assert shorten("cs50") == "cs50"


