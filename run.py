from io import BytesIO

import uvicorn
from PIL import Image
from PIL.ImageDraw import ImageDraw


class Server:
    async def __call__(self, scope, receive, send):
        path = scope["path"]

        try:
            im = self.generate_image_from_hexes(*path[1:].split("&"))
        except ValueError:
            print(f"Couldn't handle: {path}")
            await send({
                'type': 'http.response.start',
                'status': 400,
            })
            return

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'image/jpeg'],
            ]
        })

        with BytesIO() as buffer:
            im.save(buffer, format="JPEG")

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

        im = Image.new('RGB', (width, height))

        draw = ImageDraw(im)

        for i, code in enumerate(hex_codes):
            x0 = i * (width / len(hex_codes))
            x1 = x0 + (width / len(hex_codes))

            try:
                draw.rectangle((x0, 0, x1, height), fill=code)
            except ValueError:
                draw.rectangle((x0, 0, x1, height), fill=f"#{code}")

        return im


server = Server()
if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=80)
