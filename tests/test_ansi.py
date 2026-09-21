from colorize import RED, color, strip
from colorize.shortcuts import blue, red


def test_named_color(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert red("hi") == "\x1b[38;2;205;0;0mhi\x1b[0m"


def test_hex_color(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert color("hi", "#ff8800") == "\x1b[38;2;255;136;0mhi\x1b[0m"


def test_color_instance(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert color("hi", RED) == red("hi")


def test_rgb_tuple(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert color("hi", (255, 136, 0)) == color("hi", "#ff8800")


def test_bg_and_style(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    out = color("hi", fg="#000000", bg="#ffffff", bold=True)
    assert out == "\x1b[1;38;2;0;0;0;48;2;255;255;255mhi\x1b[0m"


def test_no_color_env(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert red("hi") == "hi"


def test_force_false_overrides_force_color(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert color("hi", "#ff0000", force=False) == "hi"


def test_strip(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert strip(blue("hi")) == "hi"


def test_invalid_hex(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    try:
        color("hi", "#12345")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
