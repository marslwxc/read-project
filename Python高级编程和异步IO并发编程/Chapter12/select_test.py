# 通过非阻塞IO实现http请求
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    # 建立socket连接
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setblocking(False)
    try:
        conn.connect((host, 80))
    except BlockingIOError as e:
        pass

    while True:
        try:
            conn.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close'.format(path, host).encode('utf8'))
            break
        except IOError as e:
            pass

    data = b''
    while True:
        try:
            d = conn.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')
    print(html_data)
    conn.close()


if __name__ == "__main__":
    get_url('http://www.baidu.com')