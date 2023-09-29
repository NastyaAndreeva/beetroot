import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://russianwarship.rip/api-documentation/v2/war-info') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())   
asyncio.run(main())
# import aiohttp
# import asyncio

# async def fetch_data(session, url):
#     async with session.get(url) as response:
#         print(response.status)
#         if response.status == 200:
#             return await response.json()
#         else:
#             return None

# async def main():
#     api_url = "https://russianwarship.rip/api-documentation/v2/war-info"
    
#     async with aiohttp.ClientSession() as session:
#         data = await fetch_data(session, api_url)
        
#         if data is not None:
#             # Process and work with the retrieved data here
#             print("Received data:", data)
#         else:
#             print("Failed to retrieve data from the API")

# if __name__ == "__main__":
#     asyncio.run(main())
