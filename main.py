#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — one joke pickup line,
under 200 characters, aimed at a robot or an AI.

The joke: a neural net has layers, and "training on you all night"
is the AI-flavoured version of thinking about someone. It lands
because it is a compliment that only makes sense if you know what
a neural net is — flattery with a technical wink, in one breath.
The em dash before the punchline gives the line its timing.
"""

import os
from pathlib import Path

LINE = "Are you a neural net? Because you've got layers — and I've been training on you all night."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
