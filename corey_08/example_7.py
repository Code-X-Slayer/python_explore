import asyncio
import time

async def fetch_data(param):
    await asyncio.sleep(param)
    return f"Result of {param}"

async def main():
    # manual way
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    task3 = asyncio.create_task(fetch_data(3))
    res1 = await task1
    res2 = await task2
    res3 = await task3
    print(f"Manual Results: {[res1, res2, res3]}")

    # gather coroutines
    coroutines = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(f"Coroutines Results: {results}")

    # gather tasks
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 4)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Tasks Results: {results}")

    # task group 
    async with asyncio.TaskGroup() as tg:
        results = [tg.create_task(fetch_data(i)) for i in range(1, 4)]
    print(f"Task group results: {[result.result() for result in results]}")

    print("Main coroutine done")

if __name__ == '__main__':
    t1 = time.perf_counter()

    asyncio.run(main())
    t2 = time.perf_counter()

    print(f"Time taken : {t2-t1:.3f} seconds")