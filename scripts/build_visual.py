"""Generate profile SVGs using Python 3.11+ and the standard library.

Without --fetch: generate an illustrative visual without contribution data.
With --fetch: include a snapshot of 12 complete weeks of GitHub contributions.
"""

import argparse
import datetime as dt
import html
import json
import os
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def fetch_activity():
    owner = os.environ["PROFILE_OWNER"]
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", owner):
        raise ValueError("Invalid GitHub username")

    today = dt.datetime.now(dt.timezone.utc).date()
    end = today - dt.timedelta(days=today.weekday())
    start = end - dt.timedelta(weeks=12)

    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "login": owner,
            "from": f"{start}T00:00:00Z",
            "to": f"{end - dt.timedelta(days=1)}T23:59:59Z",
        },
    }

    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": "Bearer " + os.environ["GH_TOKEN"],
            "Content-Type": "application/json",
            "User-Agent": "profile-visual",
        },
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)

    if result.get("errors") or not result.get("data", {}).get("user"):
        raise RuntimeError("GitHub did not return a valid contribution calendar")

    weeks = result["data"]["user"]["contributionsCollection"][
        "contributionCalendar"
    ]["weeks"]

    days = {}
    for week in weeks:
        for item in week["contributionDays"]:
            date = dt.date.fromisoformat(item["date"])
            count = item["contributionCount"]

            if type(count) is not int or count < 0:
                raise ValueError("Invalid contribution count")

            if start <= date < end:
                if date in days:
                    raise ValueError("Duplicate calendar date")
                days[date] = count

    if len(days) != 84:
        raise ValueError("Incomplete calendar; existing assets preserved")

    counts = [
        sum(
            days[start + dt.timedelta(days=i * 7 + j)]
            for j in range(7)
        )
        for i in range(12)
    ]

    return {
        "owner": owner,
        "start": str(start),
        "end": str(end - dt.timedelta(days=1)),
        "updated": str(today),
        "weeks": counts,
    }


def render(dark=False, mobile=False, activity=None):
    if dark:
        bg, card, ink, muted, line, blue, teal = (
            "#0d1117", "#161b22", "#e6edf3", "#9da7b3",
            "#30363d", "#79b8ff", "#6ed7c5",
        )
    else:
        bg, card, ink, muted, line, blue, teal = (
            "#ffffff", "#f6f8fa", "#182536", "#526172",
            "#d0d7de", "#185da8", "#087b70",
        )

    if mobile:
        width, height = 420, 426 if activity else 352
    else:
        width, height = 840, 314 if activity else 294

    parts = [
        (
            '<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" '
            'role="img" aria-labelledby="title desc">'
        ),
        '<title id="title">Systems + Scale + Intelligence</title>',
        (
            '<desc id="desc">'
            'Illustrative distributed ranking and retrieval-augmented '
            'generation flows. Contribution data, when present, is a '
            'separate weekly GitHub snapshot.'
            '</desc>'
        ),
        """
        <style>
          text {
            font-family: Arial, Helvetica, sans-serif;
          }
          .packet {
            stroke-dasharray: 4 28;
            animation: flow 3s linear infinite;
          }
          @keyframes flow {
            to { stroke-dashoffset: -32; }
          }
          @media (prefers-reduced-motion: reduce) {
            .packet {
              animation: none;
              display: none;
            }
          }
        </style>
        """,
        (
            f'<rect x="0.5" y="0.5" width="{width - 1}" '
            f'height="{height - 1}" rx="12" '
            f'fill="{bg}" stroke="{line}"/>'
        ),
    ]

    def text(x, y, value, size=13, color=muted, weight=400):
        parts.append(
            f'<text x="{x}" y="{y}" fill="{color}" '
            f'font-size="{size}" font-weight="{weight}">'
            f'{html.escape(str(value))}</text>'
        )

    text(24, 31, "SYSTEMS + SCALE + INTELLIGENCE", 14, ink, 700)
    text(24, 52, "Illustrative flows / motion is not live telemetry", 11)

    lanes = [
        (
            "DISTRIBUTED SYSTEMS",
            blue,
            [
                ("Kafka", "Clickstream events"),
                ("Flink", "Stream ranking"),
                ("Redis + API", "Low-latency serving"),
            ],
        ),
        (
            "APPLIED AI",
            teal,
            [
                ("BGE", "Embed input"),
                ("FAISS", "Retrieve context"),
                ("Mistral 7B", "Generate response"),
            ],
        ),
    ]

    for lane, (label, accent, nodes) in enumerate(lanes):
        text(
            24 + lane * 198 if mobile else 24,
            79 if mobile else 77 + lane * 88,
            label,
            10,
            accent,
            700,
        )

        box_width = 174 if mobile else 224

        for index, (name, caption) in enumerate(nodes):
            x = 24 + lane * 198 if mobile else 24 + index * 282
            y = 91 + index * 67 if mobile else 87 + lane * 88

            parts.append(
                f'<rect x="{x}" y="{y}" width="{box_width}" '
                f'height="48" rx="6" fill="{card}" stroke="{line}"/>'
            )
            parts.append(
                f'<rect x="{x}" y="{y + 10}" width="3" '
                f'height="28" rx="1" fill="{accent}"/>'
            )

            text(x + 14, y + 20, name, 15, ink, 700)
            text(x + 14, y + 37, caption, 11)

            if index < 2:
                if mobile:
                    center = x + box_width / 2
                    path = f"M{center} {y + 49}v17"
                    arrow = f"M{center - 3} {y + 62}l3 4 3 -4"
                else:
                    path = f"M{x + box_width + 1} {y + 24}h55"
                    arrow = f"M{x + box_width + 51} {y + 20}l5 4 -5 4"

                parts.append(
                    f'<path d="{path}" stroke="{line}" fill="none"/>'
                )
                parts.append(
                    f'<path class="packet" d="{path}" '
                    f'stroke="{accent}" stroke-width="2" fill="none"/>'
                )
                parts.append(
                    f'<path d="{arrow}" stroke="{accent}" fill="none"/>'
                )

    top = 294 if mobile else 244
    parts.append(
        f'<path d="M24 {top - 9}H{width - 24}" stroke="{line}"/>'
    )

    if activity is None:
        text(
            24, top + 14,
            "Code, experiments, and systems in progress.",
            12, ink,
        )
        text(
            24, top + 34,
            "GitHub activity appears after a successful data refresh.",
            11,
        )
    else:
        counts = activity["weeks"]
        text(
            24, top + 10,
            "GITHUB CONTRIBUTIONS / 12 COMPLETE WEEKS",
            10, muted, 700,
        )

        chart_x = 24 if mobile else 454
        baseline = top + 67 if mobile else top + 30
        step = 30 if mobile else 28
        peak = max(counts) or 1

        for index, count in enumerate(counts):
            bar_height = 32 * count / peak
            x = chart_x + index * step

            parts.append(
                f'<path d="M{x} {baseline}h{step - 7}" stroke="{line}"/>'
            )

            if count:
                parts.append(
                    f'<rect x="{x}" y="{baseline - bar_height:.2f}" '
                    f'width="{step - 7}" height="{bar_height:.2f}" '
                    f'rx="2" fill="{teal}">'
                    f'<title>Week {index + 1}: {count} contributions</title>'
                    '</rect>'
                )

        text(
            24,
            top + 88 if mobile else top + 30,
            f'{activity["start"]} to {activity["end"]} / {sum(counts)} total',
            11,
            ink,
        )
        text(
            24,
            top + 109 if mobile else top + 51,
            f'Updated {activity["updated"]} UTC / '
            f'peak {max(counts)}/wk / counts, not impact',
            10,
        )

    parts.append("</svg>")
    svg = "\n".join(parts) + "\n"
    ET.fromstring(svg)
    return svg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()

    activity = fetch_activity() if args.fetch else None
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)

    outputs = {}
    for mobile in (False, True):
        for dark in (False, True):
            name = "system-flow" + ("-mobile" if mobile else "")
            name += "-dark.svg" if dark else "-light.svg"
            outputs[assets / name] = render(dark, mobile, activity)

    if activity:
        outputs[assets / "activity.json"] = (
            json.dumps(activity, indent=2) + "\n"
        )

    # Fetch and validate every output before changing existing assets.
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")

    print(
        "Generated four SVG variants"
        + (" and activity.json" if activity else " without activity data")
    )


if __name__ == "__main__":
    main()
