from io import BytesIO

from colours import generate_image_from_hexes


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
            image = generate_image_from_hexes(*colours)
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


if __name__ == "__main__":
    import uvicorn

    server = Server()
    uvicorn.run(server, host="0.0.0.0", port=8080)
