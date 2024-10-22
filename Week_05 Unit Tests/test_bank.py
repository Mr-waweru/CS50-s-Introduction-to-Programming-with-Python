from bank import value


# Test for $0
def test_value1(): 
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("hello") == 0


# Test for $20
def test_value2():
    assert value("hi") == 20
    assert value("helo") == 20
    assert value("HELO") == 20


# Test for $100
def test_value3():
    assert value("what's us") == 100
    assert value("CS50") == 100
    assert value("012") == 100
