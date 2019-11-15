# gil:global interpreter lock 全局解释器锁
# python中一个线程对应于c语言中的一个线程
# gil使得同一时刻只有一个线程在cpu上执行字节码,无法将多个线程映射到多个cpu上执行
# gil会根据执行的字节码行数及时间片释放gil,gil在遇到io操作的时候主动释放 
total = 0
def add():
    global total
    for _ in range(1000000):
        total += 1

def desc():
    global total
    for _ in range(1000000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)