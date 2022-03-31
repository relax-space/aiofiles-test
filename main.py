import asyncio
import os

import aiofiles


async def write_chunk_to_file(sem: asyncio.Semaphore, chunk: str) -> None:
    async with sem:
        async with aiofiles.open("test.txt", mode="a") as f:
            await f.write(f'{chunk}\n')


async def main() -> None:
    # Prepare the data to write in batches
    data_chunks: list[str] = [
        "Berlin", "Germany", "Madrid", "Spain", "Rome", "Italy",
        "Washington D.C.", "USA", "Ottawa", "Canada", "Mexico City", "Mexico",
        "Tokyo", "Japan", "Beijing", "China", "Manila", "Philippines"
    ]

    # Truncate existing file
    file_path = 'test.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)

    # Launch coroutines to write batches to the file
    sem = asyncio.Semaphore(2)
    await asyncio.gather(*[write_chunk_to_file(sem, chunk) for chunk in data_chunks])

if __name__ == "__main__":
    asyncio.run(main())
