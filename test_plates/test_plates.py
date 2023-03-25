from plates import is_valid

def test_default():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True

def test_length():
    assert is_valid("CSPPP50") == False
    assert is_valid("C") == False

def test_special():
    assert is_valid("PI.13") == False

def test_first():
    assert is_valid("1C") == False
    assert is_valid("C1") == False
    assert is_valid(" C") == False
    assert is_valid("15") == False
    assert is_valid(".C") == False

def test_digits():
    assert is_valid("CS50P") == False

def test_zero():
    assert is_valid("CS05") == False