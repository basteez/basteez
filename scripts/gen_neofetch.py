#!/usr/bin/env python3
"""Generate neofetch-style terminal SVG cards (dark + light) for the profile README."""
from html import escape

# --- ASCII espresso cup with steam (11 lines) ---
LOGO = [
    "   )  )  )",
    "  (  (  (",
    "   )  )  )",
    "  __________",
    " |          |___",
    " |~~~~~~~~~~|   |",
    " |          |   |",
    " |          |___|",
    " |          |",
    " |__________|",
    "  \\________/",
]

# --- neofetch info fields: (key, value). Header handled separately. ---
FIELDS = [
    ("OS",       "JVM · Kubernetes · Docker"),
    ("Host",     "Senior Software Engineer"),
    ("Kernel",   "Java · Quarkus · Spring Boot"),
    ("Packages", "Kafka · PostgreSQL"),
    ("Shell",    "clean code & AI enthusiast"),
    ("Interests","dev ergonomics · tooling · AI"),
    ("Location", "Italy"),
    ("Terminal", "bstz.it"),
    ("Contact",  "LinkedIn · dev.to · Stack Overflow · Email"),
]
HEADER = "tiziano@bstz"

THEMES = {
    "dark": dict(
        window="#0d1117", titlebar="#161b22", border="#30363d",
        fg="#c9d1d9", dim="#8b949e", logo="#E0A458", header="#E0A458", key="#58A6FF",
        palette=["#484f58", "#ff7b72", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#39c5cf", "#b1bac4",
                 "#6e7681", "#ffa198", "#56d364", "#e3b341", "#79c0ff", "#d2a8ff", "#56d4dd", "#f0f6fc"],
    ),
    "light": dict(
        window="#ffffff", titlebar="#f6f8fa", border="#d0d7de",
        fg="#24292f", dim="#57606a", logo="#B4763B", header="#B4763B", key="#0969DA",
        palette=["#6e7781", "#cf222e", "#1a7f37", "#9a6700", "#0969da", "#8250df", "#1b7c83", "#6e7781",
                 "#8c959f", "#ff8182", "#2da44e", "#bf8700", "#54aeff", "#a475f9", "#3192aa", "#d0d7de"],
    ),
}

MONO = "'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

# geometry
W, H = 860, 480
Y0 = 90          # first content baseline
LH = 26          # line height
LOGO_X = 40
INFO_X = 380
FS = 15          # font size


def build(name, t):
    e = []
    e.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" font-family="{MONO}" role="img" '
             f'aria-label="neofetch-style profile card for {HEADER}">')
    # window
    e.append(f'<rect x="6" y="6" width="{W-12}" height="{H-12}" rx="12" '
             f'fill="{t["window"]}" stroke="{t["border"]}" stroke-width="1.5"/>')
    # title bar fill + separator
    e.append(f'<path d="M6 18 A12 12 0 0 1 18 6 H{W-18} A12 12 0 0 1 {W-6} 18 V44 H6 Z" '
             f'fill="{t["titlebar"]}"/>')
    e.append(f'<line x1="6" y1="44" x2="{W-6}" y2="44" stroke="{t["border"]}" stroke-width="1"/>')
    # traffic-light dots
    for cx, col in [(30, "#ff5f56"), (52, "#ffbd2e"), (74, "#27c93f")]:
        e.append(f'<circle cx="{cx}" cy="25" r="7" fill="{col}"/>')
    # title
    e.append(f'<text x="{W/2}" y="30" text-anchor="middle" font-size="13" '
             f'fill="{t["dim"]}">{HEADER} — neofetch</text>')

    # logo
    for i, line in enumerate(LOGO):
        y = Y0 + i * LH
        e.append(f'<text x="{LOGO_X}" y="{y}" xml:space="preserve" font-size="{FS}" '
                 f'fill="{t["logo"]}" font-weight="bold">{escape(line)}</text>')

    # info header + dashes
    e.append(f'<text x="{INFO_X}" y="{Y0}" font-size="{FS}" fill="{t["header"]}" '
             f'font-weight="bold">tiziano<tspan fill="{t["fg"]}">@</tspan>bstz</text>')
    e.append(f'<text x="{INFO_X}" y="{Y0 + LH}" font-size="{FS}" fill="{t["dim"]}" '
             f'xml:space="preserve">{"-" * len(HEADER)}</text>')

    # info fields
    for i, (k, v) in enumerate(FIELDS):
        y = Y0 + (i + 2) * LH
        e.append(f'<text x="{INFO_X}" y="{y}" font-size="{FS}">'
                 f'<tspan fill="{t["key"]}" font-weight="bold">{escape(k)}</tspan>'
                 f'<tspan fill="{t["dim"]}">: </tspan>'
                 f'<tspan fill="{t["fg"]}">{escape(v)}</tspan></text>')

    # color palette strip (two rows of 8)
    sq = 22
    gap = 4
    py1 = Y0 + (len(FIELDS) + 2) * LH + 6
    py2 = py1 + sq + gap
    for row, py in enumerate((py1, py2)):
        for col in range(8):
            idx = row * 8 + col
            x = INFO_X + col * (sq + gap)
            e.append(f'<rect x="{x}" y="{py}" width="{sq}" height="{sq}" rx="3" '
                     f'fill="{t["palette"][idx]}" stroke="{t["border"]}" stroke-width="0.75"/>')

    e.append('</svg>')
    return "\n".join(e)


import os
outdir = "/home/user/basteez/assets"
os.makedirs(outdir, exist_ok=True)
for name, t in THEMES.items():
    svg = build(name, t)
    with open(f"{outdir}/neofetch-{name}.svg", "w") as f:
        f.write(svg + "\n")
    print(f"wrote {outdir}/neofetch-{name}.svg  ({len(svg)} bytes)")
