import pytest

from colorize import Color


def test_named_member():
    assert Color.RED.r == 205
    assert Color.RED.to_hex() == "#cd0000"


def test_rgb_matches_named_member():
    assert Color.rgb(205, 0, 0) is Color.RED


def test_rgb_custom():
    custom = Color.rgb(1, 2, 3)
    assert (custom.r, custom.g, custom.b) == (1, 2, 3)
    assert custom not in list(Color)


def test_rgb_out_of_range():
    with pytest.raises(ValueError):
        Color.rgb(256, 0, 0)


def test_from_hex():
    assert Color.from_hex("#ff8800") == Color.rgb(255, 136, 0)
    assert Color.from_hex("#f80") == Color.from_hex("#ff8800")


def test_from_name_case_insensitive():
    assert Color.from_name("bright_red") is Color.BRIGHT_RED
    assert Color.from_name("BRIGHT_RED") is Color.BRIGHT_RED


def test_from_name_unknown():
    with pytest.raises(ValueError):
        Color.from_name("not_a_color")


def test_parse():
    assert Color.parse(Color.RED) is Color.RED
    assert Color.parse("red") is Color.RED
    assert Color.parse("#ff8800") == Color.rgb(255, 136, 0)
    assert Color.parse((1, 2, 3)) == Color.rgb(1, 2, 3)
    with pytest.raises(TypeError):
        Color.parse(object())
