# colorize

Tiny library for coloring terminal text.

```python
import colorize as c

print(c.red("error"))
print(c.green("ok"))
print(c.color("custom", "#ff8800"))
print(c.color("warn", fg=c.BLACK, bg="#ffcc00", bold=True))
print(c.render("plain text \\red{and this part is red}"))
```

## Layout

- `colorize.colors` — the `Color` class (`Color.rgb()`/`Color.from_hex()`/`Color.from_name()`) and the built-in `PALETTE`
- `colorize.ansi` — the `color()` function and `strip()`
- `colorize.shortcuts` — per-color functions (`red`, `bright_blue`, ...) generated from `PALETTE`
- `colorize.markup` — inline `\tag{...}` text markup via `render()`

## `Color`

`Color` is a plain class holding `r`/`g`/`b` components. Its classmethods
each construct a new `Color`:

```python
from colorize import Color

Color.rgb(255, 136, 0)         # from raw components
Color.from_hex("#ff8800")      # same, from a hex string
Color.from_name("bright_red")  # by built-in name, case-insensitive
Color.parse(value)             # coerce a Color, hex string, name, or (r, g, b) tuple
```

The package also exposes each built-in color as its own `Color` object —
`colorize.RED`, `colorize.BRIGHT_BLUE`, etc. — alongside the lowercase
`colorize.red("text")`-style shortcut functions.

## `color()`

```python
color(text, fg=None, bg=None, *, bold=False, dim=False, italic=False,
      underline=False, reverse=False, strike=False, force=None)
```

`fg`/`bg` accept a `Color`, a hex string (`"#ff8800"` or `"#f80"`), a
built-in color name (`"red"`, `"bright_blue"`), or an `(r, g, b)` tuple.

Coloring is skipped automatically when stdout isn't a tty, or when the
[`NO_COLOR`](https://no-color.org) env var is set. Set `FORCE_COLOR` to
force it on, or pass `force=True`/`force=False` per call.

`strip(text)` removes ANSI escape codes from a string.

## Inline markup

`render()` expands `\tag{...}` tags inside a string:

```python
c.render("this is some text \\red{and this part is red}")
c.render("\\bg=blue+bright_white+bold{warning}")
```

A tag is `\<spec>{text}`, where `<spec>` is a color name or hex code,
optionally combined with `bg=<color>` and/or style flags (`bold`, `dim`,
`italic`, `underline`, `reverse`, `strike`), joined with `+`. Tags don't
nest, and `{`/`}` can't appear inside a tag's text.

## Install

```
pip install -e .
```

## Test

```
pip install -e ".[test]"
pytest
```
