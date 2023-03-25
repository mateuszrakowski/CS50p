from lines import check_cli, count_lines
import pytest


def test_check_cli():
    with pytest.raises(SystemExit) as info:
        check_cli(["lines.py"])
    assert info.value.code == "Too few command-line arguments"

    with pytest.raises(SystemExit) as info:
        check_cli(["lines.py", "e"])
    assert info.value.code == "Not a Python file"

    with pytest.raises(SystemExit) as info:
        check_cli(["lines.py", "e.py"])
    assert info.value.code == "File does not exist"

    with pytest.raises(SystemExit) as info:
        check_cli(["lines.py", "e", "eee"])
    assert info.value.code == "Too many command-line arguments"

    assert check_cli(["lines.py", "test.py"]) == 2


def test_count_lines():
    assert count_lines("test.py") == 2