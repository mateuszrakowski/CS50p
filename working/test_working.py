from working import convert
import pytest


def test_valid():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("8:45 AM to 11:55 PM") == "08:45 to 23:55"
    assert convert("9 PM to 10 AM") == "21:00 to 10:00"
    assert convert("10 AM to 9 PM") == "10:00 to 21:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("00:01 PM to 9:10 AM")
    with pytest.raises(ValueError):
        convert("0:01 PM to 9:10 AM")
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("9:01 AM to 00:01 PM")
    with pytest.raises(ValueError):
        convert("9:01 AM to 0:01 PM")
    with pytest.raises(ValueError):
        convert("9:01 AM - 0:01 PM")