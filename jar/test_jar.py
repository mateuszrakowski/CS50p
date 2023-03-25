from jar import Jar
import pytest


def test_init():
    jar = Jar(3)
    assert jar.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(4)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(6)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar = Jar(6)
        jar.deposit(3)
        jar.withdraw(4)
