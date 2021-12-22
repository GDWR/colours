from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

from PIL import Image
from PIL.ImageDraw import ImageDraw


class ColourHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        colours = self.path[1:].split("&")
        im = self.generate_image_from_hexes(*colours)

        with BytesIO() as buffer:
            im.save(buffer, format="JPEG")
            self.wfile.write(buffer.getvalue())

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


if __name__ == "__main__":
    with HTTPServer(("0.0.0.0", 80), ColourHandler) as server:
        server.serve_forever()
