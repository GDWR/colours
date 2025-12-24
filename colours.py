import random
import math
from PIL import Image, ImageFont, ImageColor
from PIL.ImageDraw import ImageDraw

colour_mapping = {
    "fuschia": (255, 0, 255),
    "griff": (252, 132, 1),
    "joe": (255, 255, 255),
    "xith": (239, 57, 142),
}


def _rgb_to_hex(rgb: tuple) -> str:
    return '#%02X%02X%02X' % rgb


def _get_random_rgb():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def generate_image_from_hexes(*hex_codes: str, width: int = 1920, height: int = 1080) -> Image:
    """
    From a list of hex codes in the format #FFFFFF
    Create an image split evenly vertically depicting each colour.

    :param hex_codes: repeated param of each hex code.
    :param width: output image's width.
    :param height: output image's height.
    :return: Image
    """

    im = Image.new("RGBA", (width, height), (255, 0, 0, 0))

    fnt_size = round(40 / (len(hex_codes) / 5))
    fnt = ImageFont.truetype("LemonMilkMedium.otf", fnt_size)

    draw = ImageDraw(im)

    for i, code in enumerate(hex_codes):
        left = i * (width / len(hex_codes))
        right = left + (width / len(hex_codes))

        if code != 'random':
            try:
                colour = ImageColor.getrgb(code)
            except ValueError:
                colour = colour_mapping.get(code.lower())

            if colour is None:
                code = f"#{code}"
                colour = ImageColor.getrgb(code)
        else:
            colour = _get_random_rgb()
            code = _rgb_to_hex(colour)

        draw.rectangle((left, 0, right, height), fill=colour)
        text_im_width = math.ceil(right - left)
        text_im = Image.new(
            "RGBA", (text_im_width, math.floor(fnt_size * 1.7)), (0, 0, 0, 100)
        )
        ImageDraw(text_im).text(
            ((text_im_width // 2) - (fnt.getlength(code) // 2), 0), code, font=fnt
        )
        im.paste(text_im, box=(math.floor(left), 0), mask=text_im)

    return im
