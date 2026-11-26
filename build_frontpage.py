#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news front page (1024x1024 PNG).

Everything here is drawn with Pillow from flat shapes and text: no
network, no randomness, no downloaded assets. Re-running this script
produces the same frontpage.png every time. The six stories are the
day's news as reported on 25 November 2026.
"""

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1024, 1024)
PAPER = (248, 245, 238)
INK = (18, 18, 18)
GREY = (72, 72, 72)
RED = (178, 34, 28)
NAVY = (16, 42, 78)
SEA = (24, 58, 96)
GOLD = (232, 190, 90)
FLAME = (240, 120, 20)
EMBER = (250, 200, 60)

SERIF_BOLD = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


class Page:
    """A small drawing helper holding the canvas and its fonts."""

    def __init__(self):
        self.image = Image.new("RGB", CANVAS, PAPER)
        self.pen = ImageDraw.Draw(self.image)

    def typeface(self, path, size):
        return ImageFont.truetype(path, size)

    def split(self, text, font, width):
        """Break text into lines that fit inside width pixels."""
        words = text.split()
        lines, current = [], ""
        for word in words:
            trial = f"{current} {word}".strip()
            if self.pen.textlength(trial, font=font) <= width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines

    def block(self, x, y, text, font, width, colour=INK, gap=None):
        """Draw a wrapped paragraph, returning the y below it."""
        step = gap or int(font.size * 1.2)
        for line in self.split(text, font, width):
            self.pen.text((x, y), line, font=font, fill=colour)
            y += step
        return y

    def hrule(self, x0, y, x1, thick=3, colour=INK):
        self.pen.line([(x0, y), (x1, y)], fill=colour, width=thick)

    def save(self, name="frontpage.png"):
        self.image.save(name)
        print(f"saved {name} {self.image.size}")


def draw_masthead(page):
    big = page.typeface(SERIF_BOLD, 92)
    small = page.typeface(SANS_BOLD, 22)
    page.pen.text((512, 26), "THE WORLD", font=big, fill=INK, anchor="ma")
    page.hrule(28, 136, 996, 4)
    page.pen.text(
        (512, 144),
        "WEDNESDAY  25  NOVEMBER  2026  \u2022  WORLD NEWS IN ONE PAGE",
        font=small,
        fill=INK,
        anchor="ma",
    )
    page.hrule(28, 180, 996, 2)


def draw_lead_scene(page):
    """Burning tankers in the Strait of Hormuz, drawn as flat shapes."""
    x, y, w, h = 28, 196, 612, 196
    page.pen.rectangle([x, y, x + w, y + h], fill=SEA)
    page.pen.rectangle([x, y + 122, x + w, y + h], fill=(12, 34, 62))
    page.pen.ellipse([x + 470, y + 16, x + 532, y + 78], fill=GOLD)
    for cx, cy, r in [(110, 42, 36), (180, 26, 46), (420, 36, 40)]:
        shade = (70, 70, 70) if r > 40 else (95, 95, 95)
        page.pen.ellipse(
            [x + cx - r, y + cy - r, x + cx + r, y + cy + r], fill=shade
        )
    page.pen.rectangle([x + 60, y + 118, x + 540, y + 158], fill=(30, 30, 30))
    page.pen.rectangle([x + 420, y + 88, x + 500, y + 118], fill=(205, 205, 205))
    page.pen.rectangle([x + 90, y + 96, x + 180, y + 118], fill=RED)
    for fx, fy, fw, fh in [
        (120, 62, 46, 58),
        (180, 48, 56, 72),
        (250, 66, 44, 54),
        (330, 56, 50, 64),
        (440, 70, 40, 48),
    ]:
        page.pen.polygon(
            [
                (x + fx, y + fy + fh),
                (x + fx + fw // 2, y + fy),
                (x + fx + fw, y + fy + fh),
            ],
            fill=FLAME,
        )
        page.pen.polygon(
            [
                (x + fx + 10, y + fy + fh),
                (x + fx + fw // 2, y + fy + 18),
                (x + fx + fw - 10, y + fy + fh),
            ],
            fill=EMBER,
        )
    for wy in (168, 178):
        for wx in range(0, w, 46):
            page.pen.arc(
                [x + wx, y + wy - 8, x + wx + 44, y + wy + 8],
                200,
                340,
                fill=(120, 170, 220),
                width=3,
            )


def draw_lead_text(page):
    kicker = page.typeface(SANS_BOLD, 20)
    headline = page.typeface(SANS_BOLD, 42)
    deck = page.typeface(SANS, 21)
    page.pen.text((28, 402), "STRAIT OF HORMUZ", font=kicker, fill=RED)
    y = page.block(
        28, 430, "TANKERS ABLAZE AFTER MINE STRIKES", headline, 612, gap=50
    )
    page.block(
        28,
        534,
        "Two oil tankers hit naval mines, exploded and caught fire in "
        "the strait, Iran's IRGC said.",
        deck,
        612,
        GREY,
        gap=27,
    )


def draw_side_story(page, x, y, width, kicker, headline, deck):
    kick = page.typeface(SANS_BOLD, 18)
    head = page.typeface(SANS_BOLD, 30)
    body = page.typeface(SANS, 20)
    page.pen.text((x, y), kicker, font=kick, fill=RED)
    y = page.block(x, y + 28, headline, head, width, gap=35)
    page.block(x, y + 8, deck, body, width, GREY, gap=26)
    return y


def draw_middle(page):
    page.hrule(660, 196, 996, 2)
    draw_side_story(
        page,
        660,
        200,
        336,
        "UNITED STATES",
        "HUAWEI FOUND GUILTY IN U.S. TRIAL",
        "Jury convicts on trade-secret theft and bank fraud \u2014 "
        "not racketeering.",
    )
    page.hrule(660, 368, 996, 2)
    page.pen.rectangle([660, 382, 996, 436], fill=NAVY)
    page.pen.polygon([(700, 430), (716, 390), (732, 430)], fill=PAPER)
    page.pen.rectangle([708, 410, 724, 430], fill=FLAME)
    page.pen.ellipse([760, 396, 796, 432], fill=GOLD)
    page.pen.text(
        (808, 400), "SHENZHOU-24", font=page.typeface(SANS_BOLD, 20), fill=PAPER
    )
    draw_side_story(
        page,
        660,
        448,
        336,
        "SPACE  \u2022  CHINA",
        "PAKISTAN'S FIRST ASTRONAUT",
        "Shenzhou-24 carries the first Pakistani astronaut into orbit.",
    )


def draw_bottom_row(page):
    page.hrule(28, 610, 996, 3)
    stories = [
        (
            28,
            304,
            "SAUDI ARABIA",
            "HOUTHIS STRIKE RAS TANURA REFINERY",
            "Fires at the oil refinery; a day earlier a strike on a "
            "Riyadh skyscraper injured 11.",
            (24, 58, 96),
            "flame",
        ),
        (
            360,
            304,
            "PACIFIC",
            "SOLOMON ISLANDS SIGN AUSTRALIA TREATY",
            "Treaty bars any foreign military or security base on the "
            "Solomon Islands.",
            NAVY,
            "island",
        ),
        (
            692,
            304,
            "UKRAINE WAR",
            "ODESA STRIKE KILLS 2, INJURES 3",
            "Russian strike hits Odesa region; a child among the "
            "injured. Kyiv flat fire injures 2.",
            (60, 60, 60),
            "ruin",
        ),
    ]
    for x, w, kicker, headline, deck, band, motif in stories:
        page.pen.rectangle([x, 630, x + w, 730], fill=band)
        if motif == "flame":
            page.pen.polygon(
                [(x + 30, 718), (x + 55, 652), (x + 80, 718)], fill=FLAME
            )
            page.pen.polygon(
                [(x + 90, 718), (x + 115, 660), (x + 140, 718)], fill=EMBER
            )
            page.pen.rectangle([x + 170, 670, x + 260, 718], fill=(30, 30, 30))
        elif motif == "island":
            page.pen.ellipse([x + 30, 658, x + 150, 708], fill=(46, 125, 70))
            page.pen.ellipse([x + 180, 670, x + 260, 710], fill=(46, 125, 70))
            page.pen.text(
                (x + 8, 638),
                "NO FOREIGN BASE",
                font=page.typeface(SANS_BOLD, 18),
                fill=PAPER,
            )
        else:
            page.pen.rectangle([x + 30, 660, x + 120, 718], fill=(60, 60, 60))
            page.pen.rectangle([x + 140, 675, x + 230, 718], fill=(90, 90, 90))
            page.pen.polygon(
                [(x + 250, 718), (x + 270, 665), (x + 290, 718)], fill=FLAME
            )
        draw_side_story(page, x, 746, w, kicker, headline, deck)


def draw_footer(page):
    page.hrule(28, 986, 996, 2)
    page.pen.text(
        (512, 992),
        "Sources: Just Security \u2022 Open Chronicle \u2022 Daily Mirror  "
        "\u2022  25 November 2026",
        font=page.typeface(SANS, 16),
        fill=(90, 90, 90),
        anchor="ma",
    )


def build():
    page = Page()
    draw_masthead(page)
    draw_lead_scene(page)
    draw_lead_text(page)
    draw_middle(page)
    draw_bottom_row(page)
    draw_footer(page)
    page.save("frontpage.png")


if __name__ == "__main__":
    build()
