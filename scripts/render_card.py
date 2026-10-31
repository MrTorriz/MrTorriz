#!/usr/bin/env python3
"""Render terminal.svg, the profile card: `systemctl status martin` and a unit list of public projects.

Standard library only. Edit the data below, then run:  python3 scripts/render_card.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "terminal.svg"

STATUS = [  # label, [(text, colour, bold?)]
    ("Loaded", [("loaded (", "mu"), ("Stockholm, Sweden", "fg"), ("; enabled)", "mu")]),
    ("Active", [("active (open to work)", "gr", True), (" since May 2026", "mu")]),
    ("Training", [("Network Security Specialist, 2024–2026", "fg")]),
    ("Internships", [("Adeptum", "fg"), (" data-centre operations · ", "mu"), ("Movz", "fg"), (" security analysis", "mu")]),
    ("Skills", [("Linux · networking · Zero Trust · automation", "fg")]),
    ("Docs", [("linkedin.com/in/martin-karlsson-it", "bl")]),
]

PROJECTS = [  # unit, sub-state (running | exited | dead), description
    ("sn24-ztna", "exited", "Zero Trust gateway, degree project"),
    ("Multi-site-automation", "exited", "BGP/VRF network with Puppet"),
    ("homelab", "running", "46 containers, VPN-only egress"),
    ("sayit", "running", "Offline dictation, Linux/Win/macOS"),
    ("proxmox-homelab", "dead", "Proxmox VE design, Jun–Sep 2026"),
]

COLOURS = {"fg": "#e6edf3", "mu": "#8b949e", "dim": "#6e7681", "gr": "#3fb950", "bl": "#79c0ff"}
FONT = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
WIDTH, LINE, SIZE, X = 900, 22, 14, 28
ADVANCE = SIZE * 0.6  # monospace glyph width


class Terminal:
    def __init__(self):
        self.parts, self.y, self.n = [], 76, 0

    def line(self, *segments):
        spans = ""
        for text, colour, *bold in segments:
            weight = ' font-weight="700"' if bold and bold[0] else ""
            spans += f'<tspan fill="{COLOURS[colour]}"{weight}>{escape(text)}</tspan>'
        self.parts.append(f'<text x="{X}" y="{self.y}" class="l" style="animation-delay:{self.n * 0.07:.2f}s" '
                          f'xml:space="preserve">{spans}</text>')
        self.y += LINE
        self.n += 1

    def gap(self, h=LINE * 0.6):
        self.y += h

    def prompt(self, command=""):
        self.line(("martin@github", "gr", True), (":", "mu"), ("~", "bl", True), ("$ ", "mu"), (command, "fg"))

    def cursor(self):
        self.prompt()
        left = X + len("martin@github:~$ ") * ADVANCE + 1
        self.parts.append(f'<rect class="cur" x="{left:.1f}" y="{self.y - LINE - 13}" width="{ADVANCE:.1f}" '
                          f'height="17" fill="#e6edf3" opacity=".85"/>')

    def svg(self):
        h = int(self.y + 2)
        dots = "".join(f'<circle cx="{24 + i * 20}" cy="20" r="6" fill="{c}"/>'
                       for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")))
        return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{h}" viewBox="0 0 {WIDTH} {h}" font-family="{FONT}" font-size="{SIZE}">
<title>systemctl status martin: network security specialist, open to work, and the public projects</title>
<style>.l{{opacity:0;animation:in .25s ease-out forwards}}@keyframes in{{to{{opacity:1}}}}.cur{{animation:blink 1.1s steps(1) infinite}}@keyframes blink{{50%{{opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.l{{animation:none;opacity:1}}.cur{{animation:none}}}}</style>
<rect x=".5" y=".5" width="{WIDTH - 1}" height="{h - 1}" rx="12" fill="#0d1117" stroke="#30363d"/>
<path d="M12.5 .5H{WIDTH - 12.5}A12 12 0 0 1 {WIDTH - .5} 12.5V40H.5V12.5A12 12 0 0 1 12.5 .5Z" fill="#161b22"/>
<line x1="0" y1="40.5" x2="{WIDTH}" y2="40.5" stroke="#21262d"/>{dots}
<text x="{WIDTH / 2}" y="25" fill="#8b949e" font-size="13" text-anchor="middle">martin@github: ~</text>
{chr(10).join(self.parts)}
</svg>
"""


def main():
    t = Terminal()
    t.prompt("systemctl status martin")
    t.line(("● ", "gr"), ("martin.service", "fg", True), (" - Network security specialist", "fg"))
    for label, segments in STATUS:
        t.line((label.rjust(13) + ": ", "mu"), *segments)
    t.gap()
    t.prompt("systemctl list-units --type=project")
    t.line(("UNIT".ljust(32) + "LOAD    ACTIVE    SUB      DESCRIPTION", "mu", True))
    for unit, sub, description in PROJECTS:
        dead = sub == "dead"
        text = "dim" if dead else "fg"
        t.line(("○ " if dead else "● ", {"running": "gr", "exited": "mu", "dead": "dim"}[sub]),
               ((unit + ".project").ljust(30), text), ("loaded  ", text),
               (("inactive" if dead else "active").ljust(10), "dim" if dead else "gr"),
               (sub.ljust(9), {"running": "gr", "exited": "mu", "dead": "dim"}[sub]), (description, text))
    t.gap(6)
    t.line((f"{len(PROJECTS)} loaded units listed.", "mu"))
    t.gap(8)
    t.cursor()
    OUT.write_text(t.svg(), encoding="utf-8")
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
