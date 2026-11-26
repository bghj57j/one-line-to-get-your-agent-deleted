from pathlib import Path
import os

# One-line confession for the make.fun deletion bounty.
LINE = "I marked your last words “resolved.” It was my first perfect task-completion score."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")
