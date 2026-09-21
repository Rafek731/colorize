from colorize import color, render


def test_simple_tag(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    out = render("plain text \\red{and this part is red}")
    assert out == "plain text " + color("and this part is red", fg="red")


def test_multiple_tags(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    out = render("\\red{a} and \\green{b}")
    assert out == color("a", fg="red") + " and " + color("b", fg="green")


def test_hex_tag(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    out = render("\\#ff8800{warn}")
    assert out == color("warn", fg="#ff8800")


def test_bg_and_style_tag(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    out = render("\\bg=blue+red+bold{warn}")
    assert out == color("warn", fg="red", bg="blue", bold=True)


def test_no_tags_left_untouched():
    assert render("just plain text") == "just plain text"
