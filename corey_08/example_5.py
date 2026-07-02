import time
import asyncio

async def fetch_data(param):
    print(f"Do something with param: {param}")
    time.sleep(param)
    print(f"Done with param: {param}")
    return f"Result of param: {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    res1 = await task1
    print("Task 1 completely done")
    res2 = await task2
    print("Task 2 completely done")
    return [res1, res2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Time taken: {t2-t1 :.2f} seconds")