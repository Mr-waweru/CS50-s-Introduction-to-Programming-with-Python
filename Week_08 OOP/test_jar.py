from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0
    jar1 = Jar(4)
    assert jar1._capacity == 4
    assert jar1._size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4 
    jar.deposit(4)
    assert jar.size == 8
    jar.deposit(4)
    assert jar.size == 12 
    
    # Test depositing too many cookies (more than capacity)
    with pytest.raises(ValueError):
        jar.deposit(1)

    # Test depositing a negative number of cookies
    # with pytest.raises(ValueError):
    #     jar.deposit(-1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(4)
    assert jar.size == 8
    jar.withdraw(4)
    assert jar.size == 4
    jar.withdraw(4)
    assert jar.size == 0

    # Test withdrawing more cookies than are available
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Test withdrawing a negative number of cookies
    # with pytest.raises(ValueError):
    #     jar.withdraw(-1)