"""Core ANSI coloring: the `color()` function and helpers around it."""

from __future__ import annotations

import os
import re
import sys

from .colors import Color

_RESET = "\x1b[0m"
_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

_STYLE_CODES = {
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "reverse": "7",
    "strike": "9",
}


def _enabled() -> bool:
    if os.environ.get("NO_COLOR") is not None:
        return False
    if os.environ.get("FORCE_COLOR") is not None:
        return True
    return sys.stdout.isatty()


def color(
    text: str,
    fg: Color | str | tuple[int, int, int] | None = None,
    bg: Color | str | tuple[int, int, int] | None = None,
    *,
    bold: bool = False,
    dim: bool = False,
    italic: bool = False,
    underline: bool = False,
    reverse: bool = False,
    strike: bool = False,
    force: bool | None = None,
) -> str:
    """Wrap `text` in ANSI escape codes.

    `fg`/`bg` accept a `Color`, a hex string ("#ff8800"), a built-in color
    name ("red", "bright_blue"), or an (r, g, b) tuple.

    Coloring is skipped when stdout isn't a tty, or when the `NO_COLOR`
    env var is set (https://no-color.org). Set `FORCE_COLOR` to force it
    on, or pass `force=True`/`force=False` to override per call.
    """
    if force is False or (force is None and not _enabled()):
        return text

    codes: list[str] = []
    if bold:
        codes.append(_STYLE_CODES["bold"])
    if dim:
        codes.append(_STYLE_CODES["dim"])
    if italic:
        codes.append(_STYLE_CODES["italic"])
    if underline:
        codes.append(_STYLE_CODES["underline"])
    if reverse:
        codes.append(_STYLE_CODES["reverse"])
    if strike:
        codes.append(_STYLE_CODES["strike"])

    if fg is not None:
        c = Color.parse(fg)
        codes.append(f"38;2;{c.r};{c.g};{c.b}")
    if bg is not None:
        c = Color.parse(bg)
        codes.append(f"48;2;{c.r};{c.g};{c.b}")

    if not codes:
        return text
    return f"\x1b[{';'.join(codes)}m{text}{_RESET}"


def strip(text: str) -> str:
    """Remove ANSI escape codes from `text`."""
    return _ANSI_RE.sub("", text)
