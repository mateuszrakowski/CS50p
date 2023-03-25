from bank import value

def test_case_insensitive():
    assert value("Hello customer!") == 0
    assert value("hello friend") == 0

def test_outputs():
    assert value("whats up") == 100
    assert value("hey brian") == 20

def test_integers():
    assert value("1Hey") == 100
    assert value("Hello 523214!24./") == 0

def test_special_signs():
    assert value("../Hey") == 100