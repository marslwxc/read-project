from concurrent import futures
import time

# futures 未来对象，task的返回容器

# 线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候主线程能够立即知道
# futures可以让多线程和多进程编码接口一致

def get_html(sleep_times):
    time.sleep(sleep_times)
    print('got page {} success'.format(sleep_times))
    return sleep_times

executor = futures.ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中, submit是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# 获取已经成功的task返回 future.as_completed
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
futures.wait(all_task)
for future in futures.as_completed(all_task):
    data = future.result()
    print("get {} page success".format(data))

# 通过executor.map获取已经完成的task的值
# for data in executor.map(get_html, urls):
#     print("get {} page".format((data)))

# done方法用于判定某个任务是否完成
# print(task1.done())
# # 取消任务，返回是否成功
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# # result可以获取task的执行结果
# print(task1.result())