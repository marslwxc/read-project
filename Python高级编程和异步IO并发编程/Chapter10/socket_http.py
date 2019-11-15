# requests -> urllib -> socket
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
    conn.connect((host, 80))

    conn.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close'.format(path, host).encode('utf8'))
    data = b''
    while True:
        d = conn.recv(1024)
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