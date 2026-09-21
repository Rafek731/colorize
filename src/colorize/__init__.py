"""Tiny library for coloring terminal text.

    >>> import colorize as c
    >>> print(c.red("error"))
    >>> print(c.color("custom", "#ff8800"))
    >>> print(c.color("warn", fg=c.BLACK, bg="#ffcc00", bold=True))
    >>> print(c.render("plain text \\red{and this part is red}"))

Coloring is automatically disabled when stdout isn't a tty, or when the
NO_COLOR env var is set (https://no-color.org). Set FORCE_COLOR to force
it on regardless (e.g. when piping to something that renders ANSI).
"""

from __future__ import annotations

from .ansi import color, strip
from .color import Color
from .markup import render
from .shortcuts import (
    black, red, green, yellow, blue, magenta, cyan, white,
    bright_black, bright_red, bright_green, bright_yellow,
    bright_blue, bright_magenta, bright_cyan, bright_white,
)

# Each built-in color exposed as its own `Color` object.
BLACK = Color.from_name("black")
RED = Color.from_name("red")
GREEN = Color.from_name("green")
YELLOW = Color.from_name("yellow")
BLUE = Color.from_name("blue")
MAGENTA = Color.from_name("magenta")
CYAN = Color.from_name("cyan")
WHITE = Color.from_name("white")
BRIGHT_BLACK = Color.from_name("bright_black")
BRIGHT_RED = Color.from_name("bright_red")
BRIGHT_GREEN = Color.from_name("bright_green")
BRIGHT_YELLOW = Color.from_name("bright_yellow")
BRIGHT_BLUE = Color.from_name("bright_blue")
BRIGHT_MAGENTA = Color.from_name("bright_magenta")
BRIGHT_CYAN = Color.from_name("bright_cyan")
BRIGHT_WHITE = Color.from_name("bright_white")

__all__ = [
    "Color", "color", "strip", "render",
    "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE",
    "BRIGHT_BLACK", "BRIGHT_RED", "BRIGHT_GREEN", "BRIGHT_YELLOW",
    "BRIGHT_BLUE", "BRIGHT_MAGENTA", "BRIGHT_CYAN", "BRIGHT_WHITE",
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow",
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
]
