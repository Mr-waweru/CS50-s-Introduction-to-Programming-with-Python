from fuel import convert, gauge
import pytest


def test_convert_and_gauge():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("4/4") == 100 and gauge(100) == "F"
    assert convert("0/4") == 0 and gauge(0) == "E"
    
    
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")