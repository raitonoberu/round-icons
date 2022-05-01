from math import pi
import cairo
import yaml
import sys
import os

SIZES = [512, 256, 128, 64, 48, 32]
OFFSET = 0.4


def generate(logo: cairo.ImageSurface, color: tuple, size: int) -> cairo.ImageSurface:
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    cr = cairo.Context(surface)

    cr.set_source_rgb(*color)
    cr.arc(size / 2, size / 2, size / 2, 0, 2 * pi)
    cr.fill()

    cr.translate(size / 2 * OFFSET, size / 2 * OFFSET)
    cr.scale(
        size / logo.get_width() * (1 - OFFSET), size / logo.get_height() * (1 - OFFSET)
    )

    cr.set_source_surface(logo)
    cr.paint()

    return surface


def save(img: cairo.ImageSurface, name: str, size: int) -> None:
    if not os.path.exists(str(size)):
        os.makedirs(str(size))
    img.write_to_png(f"{size}/{name}.png")


if __name__ == "__main__":
    names = sys.argv[1:]
    icons = yaml.safe_load(open("icons.yaml"))
    for icon in icons:
        name = icon["name"]
        if names and name not in names:
            continue

        logo = cairo.ImageSurface.create_from_png(f"logos/{name}.png")
        color = [c / 255 for c in bytes.fromhex(icon["color"])]
        for size in SIZES:
            img = generate(logo, color, size)
            save(img, name, size)
