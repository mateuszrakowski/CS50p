from numb3rs import validate


def test_invalid():
    assert validate("25.275.25.11") == False
    assert validate("25.255.25.11") == True
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True