from um import count


def test_default():
    assert count("hello there, um") == 1
    assert count("um yum") == 1
    assert count("hello little mummy, yummi") == 0


def test_special_characters():
    assert count("um, hello there um.") == 2
    assert count("um! this mummy is so yummy!") == 1
    assert count("hello, excuse me um????") == 1
    assert count("hey buddy    um  ") == 1


def test_ints():
    assert count("one is 1") == 0
    assert count("123321") == 0


def test_case_insensitive():
    assert count("Um, why yuumi is so bad?") == 1
    assert count("Uma is um but mumma is not Um") == 2