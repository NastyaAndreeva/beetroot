import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('name')
    print(f"Accepted connection from {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break

        message = data.decode()
        print(f"Got: {message}")

        writer.write(data)
        await writer.drain()

    print(f"Connection from {addr} was closed")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Working on {addr[0]}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
