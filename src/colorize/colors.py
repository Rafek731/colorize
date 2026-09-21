"""The `Color` enum: built-in named colors plus arbitrary RGB/hex values."""

from __future__ import annotations

from enum import Enum


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    """Convert a hex string ("#ff8800" or "#f80") to an (r, g, b) tuple."""
    h = value.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) != 6:
        raise ValueError(f"invalid hex color: {value!r}")
    try:
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    except ValueError:
        raise ValueError(f"invalid hex color: {value!r}") from None


class Color(Enum):
    """A color: one of the built-in named colors, or an arbitrary RGB value.

        >>> Color.RED
        <Color.RED: (205, 0, 0)>
        >>> Color.rgb(255, 136, 0)
        Color.rgb(255, 136, 0)
        >>> Color.from_hex("#ff8800") == Color.rgb(255, 136, 0)
        True
    """

    BLACK = (0, 0, 0)
    RED = (205, 0, 0)
    GREEN = (0, 205, 0)
    YELLOW = (205, 205, 0)
    BLUE = (0, 0, 238)
    MAGENTA = (205, 0, 205)
    CYAN = (0, 205, 205)
    WHITE = (229, 229, 229)
    BRIGHT_BLACK = (127, 127, 127)
    BRIGHT_RED = (255, 0, 0)
    BRIGHT_GREEN = (0, 255, 0)
    BRIGHT_YELLOW = (255, 255, 0)
    BRIGHT_BLUE = (92, 92, 255)
    BRIGHT_MAGENTA = (255, 0, 255)
    BRIGHT_CYAN = (0, 255, 255)
    BRIGHT_WHITE = (255, 255, 255)

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def rgb(cls, r: int, g: int, b: int) -> Color:
        """Get a `Color` for an arbitrary RGB triplet.

        Returns the matching named member if one exists, otherwise a
        standalone `Color` carrying the given values.
        """
        for component in (r, g, b):
            if not 0 <= component <= 255:
                raise ValueError(f"color components must be in 0..255, got {(r, g, b)!r}")
        for member in cls:
            if (member.r, member.g, member.b) == (r, g, b):
                return member
        obj = object.__new__(cls)
        obj._name_ = f"rgb({r}, {g}, {b})"
        obj._value_ = (r, g, b)
        obj.r, obj.g, obj.b = r, g, b
        return obj

    @classmethod
    def from_hex(cls, value: str) -> Color:
        """Get a `Color` from a hex string like "#ff8800" or "#f80"."""
        return cls.rgb(*hex_to_rgb(value))

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
            return cls.rgb(*value)
        if isinstance(value, str):
            return cls.from_hex(value) if value.startswith("#") else cls.from_name(value)
        raise TypeError(f"cannot interpret {value!r} as a Color")

    def to_hex(self) -> str:
        """Render this color as a "#rrggbb" hex string."""
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Color):
            return (self.r, self.g, self.b) == (other.r, other.g, other.b)
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.r, self.g, self.b))

    def __repr__(self) -> str:
        if self.name in self.__class__.__members__:
            return f"Color.{self.name}"
        return f"Color.rgb({self.r}, {self.g}, {self.b})"
