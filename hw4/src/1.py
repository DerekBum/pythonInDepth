import threading
import multiprocessing
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_threads(n):
    threads = []
    start_time = time.time()
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time


def run_processes(n):
    processes = []
    start_time = time.time()
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    return end_time - start_time


def run_sync(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time


def main():
    n = 35

    with open("../artifacts/1/results.txt", "w") as file:
        file.write(f"n={n}:\n")
        file.write("Sync: {}\n".format(run_sync(n)))
        file.write("Threads: {}\n".format(run_threads(n)))
        file.write("Multiprocessors: {}\n".format(run_processes(n)))


if __name__ == "__main__":
    main()
