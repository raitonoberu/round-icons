from PIL import Image, ImageDraw
import yaml
import sys
import os

SIZES = [512, 256, 128, 64, 48, 32]
OFFSET = 0.4


def generate(logo: Image.Image, color: tuple, size: int) -> Image.Image:
    image = Image.new("RGBA", (size, size), (255, 255, 255, 0))

    circle = Image.new("RGBA", (size * 4, size * 4), (255, 255, 255, 0))
    circle_draw = ImageDraw.Draw(circle)
    circle_draw.ellipse((0, 0, size * 4, size * 4), fill=color)
    circle = circle.resize((size, size), resample=Image.Resampling.LANCZOS)

    image.paste(circle)

    offset = int(size / 2 * OFFSET)

    logo = logo.resize([int(size - offset * 2), int(size - offset * 2)])

    left_corner = (
        offset + int(size - offset * 2 - logo.size[0]),
        offset + int(size - offset * 2 - logo.size[1]),
    )
    image.paste(logo, left_corner, logo.convert("RGBA"))

    return image


def save(img: Image.Image, name: str, size: int) -> None:
    if not os.path.exists(str(size)):
        os.makedirs(str(size))
    img = img.convert("P", palette=Image.Palette.ADAPTIVE, colors=256)
    img.save(f"{size}/{name}.png", optimize=True)


if __name__ == "__main__":
    names = sys.argv[1:]
    icons = yaml.safe_load(open("icons.yaml"))
    for icon in icons:
        name = icon["name"]
        if names and name not in names:
            continue

        logo = Image.open(f"logos/{name}.png")
        color = tuple(bytes.fromhex(icon["color"]))
        for size in SIZES:
            img = generate(logo, color, size)
            save(img, name, size)