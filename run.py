import math
from io import BytesIO

import uvicorn
from PIL import Image, ImageFont, ImageColor
from PIL.ImageDraw import ImageDraw

colour_mapping = {
    "fuschia": (255, 0, 255)
}


class Server:
    async def __call__(self, scope, receive, send):
        path = scope["path"]

        if path == "/favicon.ico":
            await send({
                'type': 'http.response.start',
                'status': 404,
            })
            return

        colours = path[1:].replace("&", "-").split("-")

        try:
            im = self.generate_image_from_hexes(*colours)
        except ValueError:
            await send({
                'type': 'http.response.start',
                'status': 400,
            })
            return

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'image/png'],
            ]
        })

        with BytesIO() as buffer:
            im.save(buffer, format="PNG")

            await send({
                'type': 'http.response.body',
                'body': buffer.getvalue(),
            })

    @staticmethod
    def generate_image_from_hexes(*hex_codes: str, width: int = 1920, height: int = 1080) -> Image:
        """
        From a list of hex codes in the format #FFFFFF
        Create an image split evenly vertically depicting each colour.

        :param hex_codes: repeated param of each hex code.
        :param width: output image's width.
        :param height: output image's height.
        :return: Image
        """

        im = Image.new('RGBA', (width, height), (255, 0, 0, 0))

        fnt_size = round(40 / (len(hex_codes) / 5))
        fnt = ImageFont.truetype("LemonMilkMedium.otf", fnt_size)

        draw = ImageDraw(im)

        for i, code in enumerate(hex_codes):
            x0 = i * (width / len(hex_codes))
            x1 = x0 + (width / len(hex_codes))

            try:
                colour = ImageColor.getrgb(code)
            except ValueError:
                colour = None

            if colour is None:
                colour = colour_mapping.get(code.lower())

            if colour is None:
                code = f"#{code}"
                colour = ImageColor.getrgb(code)

            draw.rectangle((x0, 0, x1, height), fill=colour)

            text_im_width = math.ceil(x1 - x0)
            text_im = Image.new('RGBA', (text_im_width, math.floor(fnt_size * 1.7)), (0, 0, 0, 100))
            ImageDraw(text_im).text(((text_im_width // 2) - (fnt.getlength(code) // 2), 0), code, font=fnt)

            im.paste(text_im, box=(math.floor(x0), 0), mask=text_im)

        return im


server = Server()
if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=80)
