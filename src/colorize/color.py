from __future__ import annotations

from dataclasses import dataclass
from .utils import hex_to_rgb

@dataclass(frozen=True, slots=True)
class Color:
    """A color, either a named member of the `Color` enum or an arbitrary RGB triplet.
    """

    r: int
    g: int
    b: int

    def __post_init__(self) -> None:
        for component in (self.r, self.g, self.b):
            if not isinstance(component, int):
                raise TypeError(f"Color components must be integers, got {(self.r, self.g, self.b)!r}")
            if not 0 <= component <= 255:
                raise ValueError(f"Color components must be in 0..255, got {(self.r, self.g, self.b)!r}")

    @classmethod
    def from_rgb(cls, r: int, g: int, b: int) -> Color:
        """Get a `Color` for an arbitrary RGB triplet.
        """
        return cls(r, g, b)

    @classmethod
    def from_hex(cls, value: str) -> Color:
        """Get a `Color` from a hex string like "#ff8800" or "#f80"."""
        return cls.from_rgb(*hex_to_rgb(value))

    @classmethod
    def from_name(cls, name: str) -> Color:
        """Get a `Color` by its (case-insensitive) name, e.g. "bright_red"."""
        try:
            return cls[name.upper()]
        except KeyError:
            raise ValueError(f"unknown color name: {name!r}") from None

    @classmethod
    def parse(cls, value: Color | str | tuple[int, int, int]) -> Color:
        """Coerce a `Color`, hex string, color name, or (r, g, b) tuple into a `Color`."""
        if isinstance(value, cls):
            return value
        if isinstance(value, tuple):
            return cls.from_rgb(*value)
        if isinstance(value, str):
            return cls.from_hex(value) if value.startswith("#") else cls.from_name(value)
        raise TypeError(f"cannot interpret {value!r} as a Color")

    @property
    def hex(self) -> str:
        """Return this color as a "#rrggbb" hex string."""
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    @property
    def rgb(self) -> tuple[int, int, int]:
        """Return this color as an (r, g, b) tuple."""
        return (self.r, self.g, self.b)
