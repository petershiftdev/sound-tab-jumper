"""Render toolbar / store PNG icons into ../01/icons/ and copy to ../firefox/icons/.

32 and 48 are drawn 3× larger, then scaled down so the font stays readable.
16 is a pixel-hinted toolbar glyph.

Run from this folder: python render_icons.py
"""

from pathlib import Path
from shutil import copy2

from PIL import Image, ImageDraw, ImageFont

FONTS = (
    Path(r"C:\Windows\Fonts\segoeuib.ttf"),
    Path(r"C:\Windows\Fonts\arialbd.ttf"),
    Path(r"C:\Windows\Fonts\calibrib.ttf"),
)

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "01" / "icons"
FIREFOX_ICON_DIR = ROOT / "firefox" / "icons"
BG = (15, 118, 110, 255)
SPEAKER = (255, 255, 255, 255)
SIZES = (16, 32, 48, 128)
SPEAKER_RIGHT = 12


def font_path() -> Path:
    return next(path for path in FONTS if path.exists())


def draw_speaker(draw: ImageDraw.ImageDraw, cx: float, cy: float, u: float) -> None:
    body = [
        (cx - 14 * u, cy - 11 * u),
        (cx - 1 * u, cy - 11 * u),
        (cx + 12 * u, cy - 22 * u),
        (cx + 12 * u, cy + 22 * u),
        (cx - 1 * u, cy + 11 * u),
        (cx - 14 * u, cy + 11 * u),
    ]
    draw.polygon(body, fill=SPEAKER)


def plate_metrics(size: int) -> tuple[int, int, float]:
    if size >= 96:
        pad = round(size * 12 / 128)
        radius = size * 26 / 128
    elif size >= 40:
        pad = max(2, round(size * 2 / 48))
        radius = size * 11 / 48
    else:
        pad = max(1, round(size / 32))
        radius = size * 7 / 32
    inner = size - 2 * pad
    return pad, inner, radius


def render_at(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad, inner, radius = plate_metrics(size)
    draw.rounded_rectangle((pad, pad, pad + inner, pad + inner), radius=radius, fill=BG)

    speaker_h = inner * (0.80 if size >= 96 else 0.86)
    u = speaker_h / 44
    gap_px = max(4, round(inner * 0.055))
    typeface = ImageFont.truetype(str(font_path()), size=round(speaker_h * 1.02))
    qb = typeface.getbbox("?")
    qw = qb[2] - qb[0]

    scratch = Image.new("RGBA", (size * 3, size * 3), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scratch)
    ox, oy = size * 1.5, size * 1.5
    draw_speaker(sd, ox, oy, u)
    q_cx = ox + SPEAKER_RIGHT * u + gap_px + qw / 2
    sd.text((q_cx, oy + 0.2 * u), "?", fill=SPEAKER, font=typeface, anchor="mm")

    bbox = scratch.getbbox()
    if bbox is None:
        raise RuntimeError("lockup is empty")
    glyph = scratch.crop(bbox)

    max_w = inner * (0.88 if size >= 96 else 0.92)
    max_h = speaker_h
    scale = min(max_w / glyph.width, max_h / glyph.height)
    new_size = (max(1, round(glyph.width * scale)), max(1, round(glyph.height * scale)))
    glyph = glyph.resize(new_size, Image.Resampling.LANCZOS)

    plate_cx = pad + inner / 2 - inner * 0.01
    plate_cy = pad + inner / 2
    img.paste(
        glyph,
        (round(plate_cx - glyph.width / 2), round(plate_cy - glyph.height / 2)),
        glyph,
    )
    return img


def render16() -> Image.Image:
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    px = img.load()

    def put(x: int, y: int, color=SPEAKER) -> None:
        if 0 <= x < 16 and 0 <= y < 16:
            px[x, y] = color

    for y in range(16):
        for x in range(16):
            if (x in (0, 15) and y in (0, 1, 14, 15)) or (y in (0, 15) and x in (0, 1, 14, 15)):
                continue
            put(x, y, BG)

    # 2px driver + wide cone; 2px '?' with a 1px gutter.
    speaker = [
        (1, 6), (1, 7), (1, 8), (1, 9),
        (2, 6), (2, 7), (2, 8), (2, 9),
        (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
        (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11),
        (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12),
        (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12),
        (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11),
    ]
    question = [
        (9, 2), (10, 2), (11, 2), (12, 2),
        (9, 3), (10, 3), (12, 3), (13, 3),
        (12, 4), (13, 4),
        (11, 5), (12, 5),
        (10, 6), (11, 6),
        (10, 7), (11, 7),
        (10, 9), (11, 9),
        (10, 10), (11, 10),
    ]
    for x, y in speaker + question:
        put(x, y)
    return img


def union_bbox(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return (
        min(a[0], b[0]),
        min(a[1], b[1]),
        max(a[2], b[2]),
        max(a[3], b[3]),
    )


def render_128_layers() -> tuple[Image.Image, Image.Image, Image.Image]:
    """Background, speaker and '?' as separate 128×128 RGBA layers."""
    size = 128
    pad, inner, radius = plate_metrics(size)
    speaker_h = inner * 0.80
    u = speaker_h / 44
    gap_px = max(4, round(inner * 0.055))
    typeface = ImageFont.truetype(str(font_path()), size=round(speaker_h * 1.02))
    qb = typeface.getbbox("?")
    qw = qb[2] - qb[0]

    scratch_size = size * 3
    ox, oy = size * 1.5, size * 1.5
    speaker_src = Image.new("RGBA", (scratch_size, scratch_size), (0, 0, 0, 0))
    question_src = Image.new("RGBA", (scratch_size, scratch_size), (0, 0, 0, 0))
    draw_speaker(ImageDraw.Draw(speaker_src), ox, oy, u)
    ImageDraw.Draw(question_src).text(
        (ox + SPEAKER_RIGHT * u + gap_px + qw / 2, oy + 0.2 * u),
        "?",
        fill=SPEAKER,
        font=typeface,
        anchor="mm",
    )

    bbox = union_bbox(speaker_src.getbbox(), question_src.getbbox())
    if bbox is None:
        raise RuntimeError("lockup is empty")
    speaker_g = speaker_src.crop(bbox)
    question_g = question_src.crop(bbox)
    max_w = inner * 0.88
    max_h = speaker_h
    scale = min(max_w / speaker_g.width, max_h / speaker_g.height)
    new_size = (max(1, round(speaker_g.width * scale)), max(1, round(speaker_g.height * scale)))
    speaker_g = speaker_g.resize(new_size, Image.Resampling.LANCZOS)
    question_g = question_g.resize(new_size, Image.Resampling.LANCZOS)

    plate_cx = pad + inner / 2 - inner * 0.01
    plate_cy = pad + inner / 2
    xy = (round(plate_cx - speaker_g.width / 2), round(plate_cy - speaker_g.height / 2))

    background = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(background).rounded_rectangle(
        (pad, pad, pad + inner, pad + inner),
        radius=radius,
        fill=BG,
    )
    speaker = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    speaker.paste(speaker_g, xy, speaker_g)
    question = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    question.paste(question_g, xy, question_g)
    return background, speaker, question


def write_icon128_psd(path: Path) -> None:
    import numpy as np
    from pytoshop import enums
    from pytoshop.user.nested_layers import Image as PsdLayer
    from pytoshop.user.nested_layers import nested_layers_to_psd

    background, speaker, question = render_128_layers()

    def to_layer(name: str, image: Image.Image) -> PsdLayer:
        arr = np.array(image)
        return PsdLayer(
            name=name,
            top=0,
            left=0,
            bottom=image.height,
            right=image.width,
            channels={
                0: arr[:, :, 0],
                1: arr[:, :, 1],
                2: arr[:, :, 2],
                enums.ChannelId.transparency: arr[:, :, 3],
            },
        )

    # First in this list becomes the top layer in Photoshop.
    psd = nested_layers_to_psd(
        [
            to_layer("Question mark", question),
            to_layer("Speaker", speaker),
            to_layer("Background", background),
        ],
        color_mode=enums.ColorMode.rgb,
        compression=enums.Compression.raw,
        size=(128, 128),
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        psd.write(handle)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for size in SIZES:
        path = OUT_DIR / f"icon{size}.png"
        if size == 16:
            glyph = render16()
        elif size == 128:
            background, speaker, question = render_128_layers()
            glyph = Image.alpha_composite(background, speaker)
            glyph = Image.alpha_composite(glyph, question)
        else:
            glyph = render_at(size * 3).resize((size, size), Image.Resampling.LANCZOS)
        glyph.save(path, "PNG")
        print(f"wrote {path}")

    FIREFOX_ICON_DIR.mkdir(parents=True, exist_ok=True)
    for size in SIZES:
        src = OUT_DIR / f"icon{size}.png"
        dest = FIREFOX_ICON_DIR / f"icon{size}.png"
        copy2(src, dest)
        print(f"copied {dest}")

    psd_path = Path(__file__).resolve().parent / "icon128.psd"
    write_icon128_psd(psd_path)
    print(f"wrote {psd_path}")


if __name__ == "__main__":
    main()
