import multiprocessing
import time


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [10000000 + x for x in range(20)]

    start_time = time.time()
    calculate_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
# Duration 23.934669733047485 seconds