import threading
from threading import Lock


total = 0
lock = Lock()
def add():
    global total
    global lock
    for _ in range(1000000):
        lock.acquire()
        total += 1
        lock.release()

def desc():
    global total
    global lock
    for _ in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)