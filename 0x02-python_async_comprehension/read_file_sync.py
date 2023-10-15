import asyncio

async def read_file_async(file_path):
    async with open(file_path, 'r') as file:
        async for line in file:
            yield line.strip()

async def main():
    async for line in read_file_async('my_file.txt'):
        print(line)

asyncio.run(main())