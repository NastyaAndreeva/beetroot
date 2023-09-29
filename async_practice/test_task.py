import asyncio

async def print_num():
    print("Numbers")

async def print_letters():
    await print_num()
    print("Letters")

asyncio.run(print_letters())

print("111")

