from seasons import days_to_minutes
import pytest


def test_format_input():
    assert days_to_minutes("1997-12-17") == "Thirteen million, two hundred thirty-three thousand, six hundred minutes"

    with pytest.raises(SystemExit):
        days_to_minutes("17 December 1997")
        days_to_minutes("17.12.1997")
        days_to_minutes("Seventeen December 1997")


def test_wrong_date():
    with pytest.raises(SystemExit):
        days_to_minutes("1997-13-17")
        days_to_minutes("1997-12-33")
        days_to_minutes("2030-12-17")
