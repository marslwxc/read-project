# semaphore 是用于控制进入数量的锁

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('got html text success')
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for _ in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider('url', self.sem)
            html_thread.start()

if __name__ == "__main__":
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()