import asyncio
import time


async def cpu_bound(number):
    await print(sum(i * i for i in range(number)))


async def caluculate_sums(numbers):
    tasks = [asyncio.create_task(cpu_bound(number)) for number in numbers]
    await asyncio.gather(*tasks)


def main():
    start_time = time.perf_counter()
    numbers = [10000000+x for x in range(20)]
    asyncio.run(caluculate_sums(numbers))
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


if __name__ == "__main__":
    main()
