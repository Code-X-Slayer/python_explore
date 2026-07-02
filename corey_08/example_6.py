import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def fetch_data(param):
    print(f"Do Something with {param}..", flush=True)
    time.sleep(param)
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"

async def main():
    # run in threads
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    res1 = await task1
    print("Thread 1 completed")
    res2 = await task2
    print("Thread 2 completed")

    # run in process pool
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)
        res1 = await task1
        print("Process 1 completed successfully")
        res2 = await task2
        print("Process 2 completed successfully")

    return [res1, res2]

if __name__ == '__main__':
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Time taken: {t2-t1:.3f} seconds")