import asyncio
import aiohttp
import json

async def main():
    async with aiohttp.ClientSession() as session:
        rest_api = 'https://russianwarship.rip/api-documentation/v2'
        async with session.get(f'{rest_api}/war-info') as resp:
            data = await resp.json(content_type="text/html")
            # hashrate = json.load(data)
            print(data)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())   
asyncio.run(main())