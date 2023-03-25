from pizza import check_cli, menu
import pytest


def test_cli():
    with pytest.raises(SystemExit) as info:
        check_cli(["pizza.py"])
    assert info.value.code == "Too few command-line arguments"

    with pytest.raises(SystemExit) as info:
        check_cli(["pizza.py", "eee.csv", "ooo.csv"])
    assert info.value.code == "Too many command-line arguments"

    with pytest.raises(SystemExit) as info:
        check_cli(["pizza.py", "elo.py"])
    assert info.value.code == "Not a CSV file"

    with pytest.raises(SystemExit) as info:
        check_cli(["pizza.py", "test.csv"])
    assert info.value.code == "File does not exist"

    assert isinstance(check_cli(["pizza.py", "regular.csv"]), list)


def test_csv():
    assert isinstance(menu("regular.csv"), list)
