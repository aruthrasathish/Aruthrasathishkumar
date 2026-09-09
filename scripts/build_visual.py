"""Generate Aruthra's profile banner. Standard library only."""

from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def render(dark=False, mobile=False):
    colors = (
        {
            "bg": "#0d1117",
            "ink": "#edf3fa",
            "muted": "#a3b1c2",
            "line": "#29384a",
            "blue": "#8cbcff",
            "teal": "#78decb",
            "panel": "#131e2c",
            "wash": "#142b40",
        }
        if dark
        else {
            "bg": "#f7faff",
            "ink": "#14263e",
            "muted": "#52667d",
            "line": "#cbd9e8",
            "blue": "#245fc0",
            "teal": "#087f78",
            "panel": "#ffffff",
            "wash": "#e7f0fc",
        }
    )

    c = colors
    width, height = (480, 390) if mobile else (960, 300)
    parts = [
        (
            '<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" '
            'role="img" aria-labelledby="title description">'
        ),
        "<title id=\"title\">Aruthra Sathish Kumar — Software Engineer</title>",
        (
            '<desc id="description">'
            'Backend and distributed systems. Applied AI and machine learning. '
            'An abstract animated topology connects events, systems, and inference.'
            '</desc>'
        ),
        """
        <style>
          text {
            font-family: -apple-system, BlinkMacSystemFont,
                         "Segoe UI", Arial, sans-serif;
          }
          .mono {
            font-family: "SFMono-Regular", Consolas,
                         "Liberation Mono", monospace;
          }
          .packet {
            stroke-dasharray: 6 95;
            animation: travel 7s linear infinite;
          }
          .reverse {
            animation-direction: reverse;
            animation-delay: -3s;
          }
          @keyframes travel {
            to { stroke-dashoffset: -202; }
          }
          @media (prefers-reduced-motion: reduce) {
            .packet { animation: none; display: none; }
          }
        </style>
        """,
        (
            f'<rect x="1" y="1" width="{width - 2}" '
            f'height="{height - 2}" rx="18" '
            f'fill="{c["bg"]}" stroke="{c["line"]}"/>'
        ),
    ]

    def text(x, y, value, size, fill=None, weight=400,
             spacing=None, mono=False):
        attributes = (
            f'x="{x}" y="{y}" font-size="{size}" '
            f'fill="{fill or c["ink"]}" font-weight="{weight}"'
        )
        if spacing is not None:
            attributes += f' letter-spacing="{spacing}"'
        if mono:
            attributes += ' class="mono"'
        parts.append(f"<text {attributes}>{escape(value)}</text>")

    def line(path, color, stroke_width=1, extra=""):
        parts.append(
            f'<path d="{path}" fill="none" stroke="{color}" '
            f'stroke-width="{stroke_width}" stroke-linecap="round" {extra}/>'
        )

    def node(x, y, label, accent):
        parts.append(
            f'<rect x="{x}" y="{y}" width="98" height="40" '
            f'rx="9" fill="{c["panel"]}" stroke="{c["line"]}"/>'
        )
        parts.append(
            f'<circle cx="{x + 14}" cy="{y + 20}" r="3" '
            f'fill="{accent}"/>'
        )
        text(x + 25, y + 24, label, 10, c["ink"], 600, mono=True)

    if mobile:
        text(28, 36, "SYSTEMS / SCALE / INTELLIGENCE",
             10, c["blue"], 600, 1.2, True)

        text(28, 91, "Aruthra", 43, weight=700)
        text(28, 138, "Sathish Kumar", 43, weight=700)

        line("M28 160H83", c["teal"], 3)
        text(28, 194, "Software Engineer", 21, weight=600)
        text(28, 224, "Backend & Distributed Systems", 14, c["muted"])
        text(28, 247, "Applied AI / ML", 14, c["muted"])

        # Compact schematic with a second, curved route.
        route = "M126 311H191M289 311H354"
        curved = "M77 331V348Q77 358 87 358H393Q403 358 403 348V331"
        line(route, c["line"], 1.5)
        line(curved, c["line"], 1.5)
        line(route, c["blue"], 2, 'class="packet"')
        line(curved, c["teal"], 2, 'class="packet reverse"')

        node(28, 291, "EVENTS", c["blue"])
        node(191, 291, "SYSTEMS", c["blue"])
        node(354, 291, "INFERENCE", c["teal"])

    else:
        # Restrained visual field behind the topology.
        parts.append(
            f'<circle cx="789" cy="145" r="116" '
            f'fill="{c["wash"]}" opacity="0.65"/>'
        )
        for x in range(608, 925, 24):
            for y in range(40, 255, 24):
                parts.append(
                    f'<circle cx="{x}" cy="{y}" r="1" '
                    f'fill="{c["line"]}" opacity="0.6"/>'
                )

        text(36, 42, "SYSTEMS / SCALE / INTELLIGENCE",
             11, c["blue"], 600, 1.6, True)

        text(36, 107, "Aruthra", 49, weight=700)
        text(36, 161, "Sathish Kumar", 49, weight=700)

        line("M36 185H96", c["teal"], 3)
        text(36, 221, "Software Engineer", 23, weight=600)
        text(36, 251, "Backend & Distributed Systems",
             14, c["muted"])
        text(36, 274, "Applied AI / ML", 14, c["muted"])

        # Abstract topology, not a claim about a particular deployment.
        route_a = "M688 80H745Q765 80 765 100V129"
        route_b = "M765 169V198Q765 218 785 218H820"
        route_c = "M590 80H575Q561 80 561 94V204Q561 218 575 218H820"
        route_d = "M814 149H894Q908 149 908 135V94Q908 80 894 80H688"

        for route in (route_a, route_b, route_c, route_d):
            line(route, c["line"], 1.5)

        line(route_a, c["blue"], 2, 'class="packet"')
        line(route_b, c["teal"], 2, 'class="packet reverse"')
        line(route_c, c["teal"], 2, 'class="packet"')
        line(route_d, c["blue"], 2, 'class="packet reverse"')

        node(590, 60, "EVENTS", c["blue"])
        node(716, 129, "SYSTEMS", c["blue"])
        node(820, 198, "INFERENCE", c["teal"])

        text(626, 271, "BUILD / CONNECT / REASON",
             10, c["muted"], 500, 1.5, True)

    parts.append("</svg>")
    result = "\n".join(parts) + "\n"
    ET.fromstring(result)
    return result


def main():
    ASSETS.mkdir(exist_ok=True)

    outputs = {}
    for mobile in (False, True):
        for dark in (False, True):
            filename = "system-flow"
            if mobile:
                filename += "-mobile"
            filename += "-dark.svg" if dark else "-light.svg"
            outputs[ASSETS / filename] = render(dark, mobile)

    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        print(f"Generated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
