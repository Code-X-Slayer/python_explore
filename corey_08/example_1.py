import time

def fetch_data(param):
    print(f"Do something with param: {param}")
    time.sleep(param)
    print(f"Done with param: {param}")
    return f"Result of param: {param}"

def main():
    res1 = fetch_data(1)
    print("Fetch 1 completed successfully")
    res2 = fetch_data(2)
    print("Fetch 2 completed successfully")
    return [res1, res2]

t1 = time.perf_counter()

results = main()
print(results)

t2 = time.perf_counter()
print(f"Time taken: {t2-t1 :.2f} seconds")