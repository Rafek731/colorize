"""Per-color convenience functions, e.g. `red("text")`, generated from `PALETTE`."""

from __future__ import annotations

from .ansi import color
from .color import Color, PALETTE

__all__ = list(PALETTE)


def _make(name: str, member: Color):
    def fn(text: str, **kwargs) -> str:
        return color(text, fg=member, **kwargs)

    fn.__name__ = fn.__qualname__ = name
    fn.__doc__ = f"Color `text` {name.replace('_', ' ')} ({member.to_hex()})."
    return fn


for _name, _rgb in PALETTE.items():
    globals()[_name] = _make(_name, Color.rgb(*_rgb))

del _name, _rgb
