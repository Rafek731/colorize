"""Inline color markup: `render("plain text \\red{and this part is red}")`."""

from __future__ import annotations

import re

from .ansi import color

_TAG_RE = re.compile(r"\\([A-Za-z0-9_+=#]+)\{([^{}]*)\}")
_STYLE_NAMES = {"bold", "dim", "italic", "underline", "reverse", "strike"}


def _parse_spec(spec: str) -> dict:
    kwargs: dict = {}
    for part in spec.split("+"):
        if not part:
            continue
        if part in _STYLE_NAMES:
            kwargs[part] = True
        elif part.startswith("bg="):
            kwargs["bg"] = part[3:]
        else:
            kwargs["fg"] = part
    return kwargs


def render(text: str) -> str:
    """Render inline color tags in `text`.

    Tags look like `\\<spec>{...}`, where `<spec>` is a color name or hex
    code ("red", "#ff8800"), optionally combined with `bg=<color>` and/or
    style flags (bold, dim, italic, underline, reverse, strike), joined
    with "+":

        >>> render("this is some text \\red{and this part is red}")
        >>> render("\\bg=blue+bright_white+bold{warning}")

    Tags don't nest, and braces can't appear inside a tag's text.
    """

    def repl(match: re.Match[str]) -> str:
        spec, inner = match.group(1), match.group(2)
        return color(inner, **_parse_spec(spec))

    return _TAG_RE.sub(repl, text)
