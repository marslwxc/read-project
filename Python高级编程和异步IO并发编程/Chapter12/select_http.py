# 使用select实现http请求
# select + 回调 + 事件循环
# 并发性高
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ


selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.conn.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close' \
            .format(self.path, self.host).encode('utf8'))
        selector.register(self.conn.fileno(), EVENT_READ, self.readable)

    def readable(self, key): 
        d = self.conn.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)

        data = self.data.decode('utf8')
        html_data = data.split('\r\n\r\n')
        print(html_data)
        self.conn.close()
        urls.remove(self.spider_url)
        if not urls:
            global stop
            stop = True
        
    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == '':
            self.path = '/'

        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setblocking(False)

        try:
            self.conn.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册到select中
        selector.register(self.conn.fileno(), EVENT_WRITE, self.connected)

def loop():
    """
    事件循环，不停的请求socket的状态并调用对应的回调函数
    """
    # 1.select本身是不支持register模式，
    # 2.socket状态变化之后的回调是由程序员完成的
    global stop
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调 + 事件循环 + select(poll/epoll)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()