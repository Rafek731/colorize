"""Per-color convenience functions, e.g. `red("text")`, generated from `Color`."""

from __future__ import annotations

from .ansi import color
from .colors import Color

__all__ = [member.name.lower() for member in Color]


def _make(member: Color):
    def fn(text: str, **kwargs) -> str:
        return color(text, fg=member, **kwargs)

    fn.__name__ = fn.__qualname__ = member.name.lower()
    fn.__doc__ = f"Color `text` {member.name.lower().replace('_', ' ')} ({member.to_hex()})."
    return fn


for _member in Color:
    globals()[_member.name.lower()] = _make(_member)

del _member
