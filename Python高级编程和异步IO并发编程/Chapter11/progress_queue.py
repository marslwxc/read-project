from multiprocessing import Process, Queue, Manager, Pool, Pipe
import time


# def producer(queue):
#     queue.put('a')
#     time.sleep(2)

# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)

def producer(pipe):
    pipe.send('bobby')

def consumer(pipe):
    time.sleep(2)
    print(pipe.recv())


if __name__ == "__main__":
    # queue = Queue()
    # my_producer = Process(target=producer, args=(queue,))
    # my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # multiprocessing.Queue不能用于进程池中,进程池中使用Manager().Queue()
    # queue = Manager().Queue(10)
    # pool = Pool(2)
    # pool.apply_async(producer, args=(queue,))
    # pool.apply_async(consumer, args=(queue,))
    # pool.close()
    # pool.join()

    # 通过Pipe实现进程间通信,pipe只能适用于两个指定进程
    # pipe的性能高于queue
    # receive_pipe, send_pipe = Pipe()
    # my_producer = Process(target=producer, args=(send_pipe,))
    # my_consumer = Process(target=consumer, args=(receive_pipe,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()