import math
import concurrent.futures
import logging
import time
import multiprocessing

artifacts = "../artifacts/2/"

logging.basicConfig(level=logging.INFO, filename=artifacts+'2.log', filemode='w', format='%(asctime)s - %(message)s')

ITERS = 100000


def integrate(f, a, b, id_, n_iter):
    acc = 0
    num = n_iter // 10
    step = (b - a) / n_iter
    for i in range(n_iter):
        if i % num == 0:
            logging.info(f"Job #{id_} did {i} iterations")
        acc += f(a + i * step) * step
    return acc


def integrate_threaded(f, a, b, *, n_jobs=1, n_iter=ITERS):
    acc = 0
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    futures = []

    logging.info(f'Starting {n_jobs} threads...')

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = i * chunk_size
            end = start + chunk_size if i != n_jobs - 1 else n_iter
            futures.append(executor.submit(integrate, f, a + start * step, a + end * step, i, chunk_size))

    for future in concurrent.futures.as_completed(futures):
        acc += future.result()

    return acc


def integrate_multiprocessed(f, a, b, *, n_jobs=1, n_iter=ITERS):
    acc = 0
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    futures = []

    logging.info(f'Starting {n_jobs} processes...')

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = i * chunk_size
            end = start + chunk_size if i != n_jobs - 1 else n_iter
            futures.append(executor.submit(integrate, f, a + start * step, a + end * step, i, chunk_size))

    for future in concurrent.futures.as_completed(futures):
        acc += future.result()

    return acc


def time_comparison(f, a, b, n_jobs_list, executor):
    results = []
    for n_jobs in n_jobs_list:
        logging.info(f"Start of {n_jobs} jobs:\n")

        start_time = time.time()
        result = executor(f, a, b, n_jobs=n_jobs)
        end_time = time.time()
        results.append((n_jobs, end_time - start_time))
    return results


def main():
    a, b = 0, math.pi / 2
    cpu_num = multiprocessing.cpu_count()
    n_jobs_list = range(1, 2 * cpu_num + 1)

    thread_results = time_comparison(math.cos, a, b, n_jobs_list, integrate_threaded)
    process_results = time_comparison(math.cos, a, b, n_jobs_list, integrate_multiprocessed)

    with open(artifacts + "results.txt", "w") as file:
        for i, result in thread_results:
            file.write(f"ThreadPoolExecutor time, {n_jobs_list[i - 1]} jobs: {result}\n")
        file.write("\n")
        for i, result in process_results:
            file.write(f"ProcessPoolExecutor time, {n_jobs_list[i - 1]}: {result}\n")


if __name__ == "__main__":
    main()
