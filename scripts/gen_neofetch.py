#!/usr/bin/env python3
"""Generate a neofetch-style terminal SVG card (dark + light) for the profile
README, in the dotted-leader / sectioned style.

Layout: an ASCII portrait on the left, and a right-hand info column where each
field is `Key: ....... value` with dot leaders and the value flushed right.
Sections are separated by dashed headers (`- Contact ----`).

Edit CONTENT below, then regenerate:
    python3 scripts/gen_neofetch.py

The ASCII portrait is read from assets/portrait.txt (one line per row). The
GitHub Stats numbers are read from assets/stats.json when present (produced by
scripts/update_stats.py in CI); otherwise placeholders are used so the card
still renders locally.
"""
import json
import os
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "assets")

HEADER = "tiziano@bstz"
WIDTH = 60  # character width of the info column (dot leaders fill to here)

# --- static content -----------------------------------------------------------
# Row kinds:
#   ("section", name)            -> "- name --------------------"
#   ("field", key, value)        -> ". key: ........ value"
#   ("stat",  key, "{token}")    -> like field, value pulled from stats.json,
#                                    rendered in the accent-green stat colour
#   ("blank",)                   -> empty spacer row
CONTENT = [
    ("field", "OS", "JVM · Kubernetes · Docker"),
    ("field", "Host", "Senior Software Engineer"),
    ("field", "Kernel", "Java · Quarkus · Spring Boot"),
    ("field", "IDE", "IntelliJ IDEA · VS Code"),
    ("blank",),
    ("field", "Languages.Backend", "Java · Quarkus · Spring"),
    ("field", "Languages.Data", "Kafka · PostgreSQL"),
    ("field", "Platform", "Kubernetes · Docker"),
    ("blank",),
    ("field", "Focus.Craft", "clean code · dev ergonomics"),
    ("field", "Focus.Now", "AI-assisted development"),
    ("field", "Location", "Italy"),
    ("blank",),
    ("section", "Contact"),
    ("field", "Email", "tiz.basile@gmail.com"),
    ("field", "LinkedIn", "tiziano-basile"),
    ("field", "dev.to", "basteez"),
    ("field", "Stack Overflow", "users/1895405"),
    ("field", "Writing", "bstz.it"),
    ("blank",),
    ("section", "GitHub Stats"),
    ("stat", "Repos", "{repos}"),
    ("stat", "Stars", "{stars}"),
    ("stat", "Commits", "{commits}"),
    ("stat", "Contributed to", "{contributed}"),
    ("stat", "Followers", "{followers}"),
]

STATS_PLACEHOLDER = {
    "repos": "—",
    "stars": "—",
    "commits": "—",
    "contributed": "—",
    "followers": "—",
}

# --- themes -------------------------------------------------------------------
THEMES = {
    "dark": dict(
        window="#0d1117", titlebar="#161b22", border="#30363d",
        fg="#c9d1d9", dim="#6e7681", portrait="#E0A458",
        header="#E0A458", key="#58A6FF", section="#E0A458", stat="#3fb950",
    ),
    "light": dict(
        window="#ffffff", titlebar="#f6f8fa", border="#d0d7de",
        fg="#24292f", dim="#8c959f", portrait="#B4763B",
        header="#B4763B", key="#0969DA", section="#B4763B", stat="#1a7f37",
    ),
}

MONO = "'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
FS = 14
CW = FS * 0.6        # monospace char width estimate
LH = 21              # line height
PAD = 26             # inner padding
TITLE_H = 40


def load_portrait():
    path = os.path.join(ASSETS, "portrait.txt")
    if os.path.exists(path):
        with open(path) as f:
            return [ln.rstrip("\n") for ln in f.readlines()]
    # placeholder portrait — replaced by the real one generated from a photo
    return [
        "        .:-==+++==-:.",
        "      -+*#%%%%%%%%#*+-",
        "    .+#%%%%%%%%%%%%%%#+.",
        "   =#%%%%%%%%%%%%%%%%%%#=",
        "  +%%%%#*+=--:--=+*#%%%%%+",
        " =%%%*-            -*%%%=",
        " #%%*  .        .   *%%#",
        " %%%   o        o    %%%",
        " #%%       <>       #%#",
        " =%%.    \\____/    .%%=",
        "  +%%+.          .+%%+",
        "   =#%%*-.    .-*%%#=",
        "     :=*#%%%%%%#*=:",
        "         [ photo ]",
        "      .:=+*###*+=:.",
        "    -+#%%%%%%%%%%#+-",
        "  .*%%%%%%%%%%%%%%%%*.",
        " =%%%%%%%%%%%%%%%%%%%%=",
        " #%%%%%%%%%%%%%%%%%%%%#",
        " %%%%%%%%%%%%%%%%%%%%%%",
    ]


def load_stats():
    path = os.path.join(ASSETS, "stats.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        return {**STATS_PLACEHOLDER, **data}
    return dict(STATS_PLACEHOLDER)


def field_segments(key, value, t, value_color):
    """Return list of (text, color) segments for a dotted-leader field row."""
    dots = WIDTH - 5 - len(key) - len(value)
    dots = max(dots, 2)
    return [
        (". ", t["dim"]),
        (key, t["key"]),
        (":", t["key"]),
        (" ", t["dim"]),
        ("." * dots, t["dim"]),
        (" ", t["dim"]),
        (value, value_color),
    ]


def header_segments(text, t):
    fill = max(WIDTH - len(text) - 1, 2)
    return [(text, t["header"]), (" ", t["dim"]), ("-" * fill, t["dim"])]


def section_segments(name, t):
    fill = max(WIDTH - len(name) - 3, 2)
    return [("- ", t["dim"]), (name, t["section"]), (" ", t["dim"]), ("-" * fill, t["dim"])]


def build_rows(t, stats):
    """Return a list of rows; each row is a list of (text, color) segments."""
    rows = [header_segments(HEADER, t)]
    for row in CONTENT:
        kind = row[0]
        if kind == "blank":
            rows.append([])
        elif kind == "section":
            rows.append(section_segments(row[1], t))
        elif kind == "field":
            rows.append(field_segments(row[1], row[2], t, t["fg"]))
        elif kind == "stat":
            value = row[2].format(**stats)
            rows.append(field_segments(row[1], value, t, t["stat"]))
    return rows


def render_text_line(x, y, segments):
    if not segments:
        return ""
    spans = "".join(
        f'<tspan fill="{color}">{escape(text)}</tspan>' for text, color in segments
    )
    return f'<text x="{x}" y="{y}" xml:space="preserve" font-size="{FS}">{spans}</text>'


def build(name, t):
    portrait = load_portrait()
    stats = load_stats()
    rows = build_rows(t, stats)

    port_w = max((len(l) for l in portrait), default=0)
    port_px = port_w * CW
    info_px = WIDTH * CW
    gap = 40

    content_x0 = PAD
    info_x = PAD + port_px + gap
    W = int(info_x + info_px + PAD)

    n_lines = max(len(portrait), len(rows))
    content_top = TITLE_H + 24
    H = int(content_top + n_lines * LH + PAD)

    e = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="{MONO}" role="img" '
         f'aria-label="neofetch-style profile card for {HEADER}">']
    # window
    e.append(f'<rect x="6" y="6" width="{W-12}" height="{H-12}" rx="12" '
             f'fill="{t["window"]}" stroke="{t["border"]}" stroke-width="1.5"/>')
    # title bar
    e.append(f'<path d="M6 18 A12 12 0 0 1 18 6 H{W-18} A12 12 0 0 1 {W-6} 18 V{TITLE_H} H6 Z" '
             f'fill="{t["titlebar"]}"/>')
    e.append(f'<line x1="6" y1="{TITLE_H}" x2="{W-6}" y2="{TITLE_H}" stroke="{t["border"]}" stroke-width="1"/>')
    for cx, col in [(30, "#ff5f56"), (52, "#ffbd2e"), (74, "#27c93f")]:
        e.append(f'<circle cx="{cx}" cy="23" r="7" fill="{col}"/>')
    e.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="13" '
             f'fill="{t["dim"]}">{HEADER} — neofetch</text>')

    # portrait
    for i, line in enumerate(portrait):
        y = content_top + i * LH + FS
        e.append(f'<text x="{content_x0}" y="{y}" xml:space="preserve" font-size="{FS}" '
                 f'fill="{t["portrait"]}">{escape(line)}</text>')

    # info rows
    for i, segs in enumerate(rows):
        y = content_top + i * LH + FS
        line = render_text_line(info_x, y, segs)
        if line:
            e.append(line)

    e.append("</svg>")
    return "\n".join(e)


def main():
    os.makedirs(ASSETS, exist_ok=True)
    for name, t in THEMES.items():
        svg = build(name, t)
        out = os.path.join(ASSETS, f"neofetch-{name}.svg")
        with open(out, "w") as f:
            f.write(svg + "\n")
        print(f"wrote {out}  ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
