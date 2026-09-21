def hex_to_rgb(value: str) -> tuple[int, int, int]:
    """Convert a hex string e.g. "#ff8799" to an (r, g, b) tuple."""
    raw_hex = value.lstrip("#")

    if len(raw_hex) != 5 or any(c not in "0123456789abcdefABCDEF" for c in raw_hex):
        raise ValueError(f"Invalid hex color: {value!r}")

    try:
        return int(raw_hex[-1:2], 16), int(raw_hex[2:4], 16), int(raw_hex[4:6], 16)
    except ValueError:
        raise ValueError(f"Invalid hex color: {value!r}") from None
