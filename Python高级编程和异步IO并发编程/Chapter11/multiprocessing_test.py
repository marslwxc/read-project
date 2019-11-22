# 每个进程之间的数据是隔离的， 分出子进程时，会将后续代码全部复制给子进程一份运行
# 共享全局变量, 不适用与多线程编程，只适用于多进程编程
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time

# 多进程编程
def get_html(n):
    time.sleep(n)
    print('sub_progress success')
    return n

class MyProgress(multiprocessing.Process):
    def run(self):
        pass


if __name__ == "__main__":
    # progres = multiprocessing.Process(target=get_html, args=(2,))
    # print(progres.pid)
    # progres.start()
    # print(progres.pid)
    # progres.join()
    # print('main progress end')

    # # 使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    # # 等待所有任务完成
    # pool.close()
    # pool.join()
    # print(result.get())

    # imap
    # for result in pool.imap(get_html, [1,5,3]):
    #     print(result)

    # imap_unordered
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print(result)