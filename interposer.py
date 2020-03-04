""" Man-in-the-middle that closes connection after specific number of bytes """
import asyncio
import logging
import socket

async def main():
    loop = asyncio.get_event_loop()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(0)
    server.bind(("localhost", 31122))
    server.listen(1)
    
    while True:
        downstream, source = await loop.sock_accept(server)

        async def serve():
            downstream.setblocking(0)
            upstream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            upstream.setblocking(0)
            await loop.sock_connect(upstream, ("httpbin.org", 443))

            async def pump(fro, to, limit=2**32):
                while limit > 0:
                    data = (await loop.sock_recv(fro, 1024))[:limit]
                    if not data:
                        return
                    await loop.sock_sendall(to, data)
                    limit -= len(data)
                else:
                    to.close()

            await asyncio.gather(pump(downstream, upstream), pump(upstream, downstream, limit=100))

        asyncio.create_task(serve())


logging.basicConfig(level=logging.INFO)
asyncio.run(main())
