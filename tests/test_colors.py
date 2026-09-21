import pytest

from colorize.color import Color


def test_rgb():
    color = Color.rgb(205, 0, 0)
    assert (color.r, color.g, color.b) == (205, 0, 0)
    assert color.to_hex() == "#cd0000"


def test_rgb_out_of_range():
    with pytest.raises(ValueError):
        Color.rgb(256, 0, 0)


def test_from_hex():
    assert Color.from_hex("#ff8800") == Color.rgb(255, 136, 0)
    assert Color.from_hex("#f80") == Color.from_hex("#ff8800")


def test_from_name_case_insensitive():
    assert Color.from_name("bright_red") == Color.rgb(255, 0, 0)
    assert Color.from_name("BRIGHT_RED") == Color.from_name("bright_red")


def test_from_name_unknown():
    with pytest.raises(ValueError):
        Color.from_name("not_a_color")


def test_parse():
    red = Color.from_name("red")
    assert Color.parse(red) == red
    assert Color.parse(red) is not red  # classmethods always construct a new Color
    assert Color.parse("red") == red
    assert Color.parse("#ff8800") == Color.rgb(255, 136, 0)
    assert Color.parse((1, 2, 3)) == Color.rgb(1, 2, 3)
    with pytest.raises(TypeError):
        Color.parse(object())


def test_equality_and_hash():
    assert Color.rgb(1, 2, 3) == Color.rgb(1, 2, 3)
    assert hash(Color.rgb(1, 2, 3)) == hash(Color.rgb(1, 2, 3))
