"""Tiny library for coloring terminal text.

    >>> import colorize as c
    >>> print(c.red("error"))
    >>> print(c.color("custom", "#ff8800"))
    >>> print(c.color("warn", fg=c.Color.BLACK, bg="#ffcc00", bold=True))
    >>> print(c.render("plain text \\red{and this part is red}"))

Coloring is automatically disabled when stdout isn't a tty, or when the
NO_COLOR env var is set (https://no-color.org). Set FORCE_COLOR to force
it on regardless (e.g. when piping to something that renders ANSI).
"""

from __future__ import annotations

from .ansi import color, strip
from .colors import Color
from .markup import render
from .shortcuts import (
    black, red, green, yellow, blue, magenta, cyan, white,
    bright_black, bright_red, bright_green, bright_yellow,
    bright_blue, bright_magenta, bright_cyan, bright_white,
)

__all__ = [
    "Color", "color", "strip", "render",
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow",
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
]
