import math
from PIL import Image, ImageFont, ImageColor
from PIL.ImageDraw import ImageDraw
from io import BytesIO

colour_mapping = {
    "fuschia": (255, 0, 255),
    "griff": (252, 132, 1)
}


class Server:
    """ASGI Server implementation."""

    async def __call__(self, scope, receive, send):
        path = scope["path"]

        if path == "/favicon.ico":
            await send(
                {
                    "type": "http.response.start",
                    "status": 404,
                }
            )
            return

        colours = path[1:].replace("&", "-").split("-")

        try:
            image = self.generate_image_from_hexes(*colours)
        except ValueError:
            await send(
                {
                    "type": "http.response.start",
                    "status": 400,
                }
            )
            return

        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"image/png"],
                ],
            }
        )

        with BytesIO() as buffer:
            image.save(buffer, format="PNG")

            await send(
                {
                    "type": "http.response.body",
                    "body": buffer.getvalue(),
                }
            )

    @staticmethod
    def generate_image_from_hexes(
            *hex_codes: str, width: int = 1920, height: int = 1080
    ) -> Image:
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

            try:
                colour = ImageColor.getrgb(code)
            except ValueError:
                colour = None

            if colour is None:
                colour = colour_mapping.get(code.lower())

            if colour is None:
                code = f"#{code}"
                colour = ImageColor.getrgb(code)

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


if __name__ == "__main__":
    import os
    import uvicorn

    server = Server()

    uvicorn.run(server, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
