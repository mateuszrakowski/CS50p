from fuel import gauge
from fuel import convert
import pytest


def test_zero_one():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_default_gauge():
    assert gauge(10) == "10%"
    assert gauge(50) == "50%"
    assert gauge(95) == "95%"
    assert gauge(4) == "4%"

def test_default_convert():
    assert convert("1/10") == 10
    assert convert("5/100") == 5
    assert convert("90/100") == 90

def test_wrong_input():
    with pytest.raises(ValueError):
        convert("elo")
    with pytest.raises(ZeroDivisionError):
        convert("6/0")
    with pytest.raises(ValueError):
        convert("elo/xd")
