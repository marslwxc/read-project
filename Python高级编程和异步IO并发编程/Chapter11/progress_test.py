# 多进程编程
# 耗cpu的操作用多进程编程，对于IO操作使用多线程编程
# 进程的切换比线程切换的代价要高
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import time
# 对于耗费CPU的操作：计算的操作
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# 对于IO来说
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25,35)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print(data)
    #     print(time.time()-start_time) # 75.57050371170044
    # 多进程
    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25,35)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print(data)
    # print(time.time() - start_time)  # 4.80504584312439
    # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print(data)
    #     print(time.time()-start_time) # 20.05365538597107
    # 多进程
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print(data)
    print(time.time() - start_time)  # 20.240546703338623