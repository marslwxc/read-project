
浏览器输入一个url中间经历的过程
1. DNS查询
2. TCP握手
3. HTTP请求
4. 反向代理Nginx
5. uwsgi
6. web app 响应
7. TCP握手

TCP的三次握手

三次握手
1. 客户端通过向服务器端发送一个SYN来创建一个主动打开，作为三次握手的一部分。客户端把这段连接的序号设定为随机数 A。
2. 服务器端应当为一个合法的SYN回送一个SYN/ACK。ACK 的确认码应为 A+1，SYN/ACK 包本身又有一个随机序号 B。
3. 最后，客户端再发送一个ACK。当服务端受到这个ACK的时候，就完成了三路握手，并进入了连接创建状态。此时包序号被设定为收到的确认号 A+1，而响应则为 B+1。

四次挥手

注意: 中断连接端可以是客户端，也可以是服务器端. 下面仅以客户端断开连接举例, 反之亦然.

1. 客户端发送一个数据分段, 其中的 FIN 标记设置为1. 客户端进入 FIN-WAIT 状态. 该状态下客户端只接收数据, 不再发送数据.
2. 服务器接收到带有 FIN = 1 的数据分段, 发送带有 ACK = 1 的剩余数据分段, 确认收到客户端发来的 FIN 信息.
3. 服务器等到所有数据传输结束, 向客户端发送一个带有 FIN = 1 的数据分段, 并进入 CLOSE-WAIT 状态, 等待客户端发来带有 ACK = 1 的确认报文.
4. 客户端收到服务器发来带有 FIN = 1 的报文, 返回 ACK = 1 的报文确认, 为了防止服务器端未收到需要重发, 进入 TIME-WAIT 状态. 服务器接收到报文后关闭连接. 客户端等待 2MSL 后未收到回复, 则认为服务器成功关闭, 客户端关闭连接.

TCP/UDP
- 面向连接、可靠的、基于字节流
- 无连接、不可靠、面向报文

## HTTP常考题
HTTP请求的组成
- 状态行
    1. 请求方法
    2. 路径
    3. HTTP版本
- 请求头
    1. 接受编码
    2. 接受类型
    3. 编码
    4. HOST
    5. 请求代理
- 消息主体

HTTP响应的组成
- 状态行
    1. HTTP版本
    2. 状态码
- 响应头
- 响应正文
    1. HTML

HTTP常见状态码
- 1\*\*信息，服务器收到请求，需要请求者继续执行操作
- 2\*\*成功，操作被成功接受并处理
    - 200 OK
- 3\*\*重定向，需要进一步操作完成请求
    - 301 永久重定向
    - 302 临时重定向
- 4\*\*客户端错误，请求有语法错误或者无法完成请求
    - 400 请求包含错误的语法，请求错误
    - 401 未认证
    - 403 被禁止
    - 404 Not Found
    - 405 web框架未定义HTTP方法
- 5\*\*服务器错误，服务器在处理请求的过程中欧冠发生错误
    - 500 internal server error

常见HTTP方法：
- GET：获取
- POST：创新
- PUT：更新
- DELETE：删除

HTTP GET/POST区别
- Restful语义上一个是获取，一个是创建
- GET是幂等的，POST非幂等
- GET请求参数放到url，长度限制；POST放在请求体，更安全

幂等
- 幂等方法是无论调用多少次都得到相同结果的HTTP方法
- 例如：a=4是幂等，a+=4是非幂等
- 幂等方法客户端可以安全地重发请求

HTTP Method | Idempotent | Safe
----------- | ---------- | ----
OPTIONS | yes | yes
GET | yes | yes
HEAD | yes | yes
PUT | yes | no
POST | no | no
DELETE | yes | no
PATCH | no | no

什么是HTTP长连接
- 短连接：建立连接 - 数据传输 - 关闭连接（连接的建立和关闭开销大）
- 长连接：保持TCP连接不断开
- Request Headers/Connections：keep-alive
- 如何区分不同的HTTP请求:Content-Length | Transfer-Encoding:chunked

cookie 和 session 区别
- Session一般是服务器生成之后给客户端（通过url参数或cookie）
- Cookie是实现session的一种机制，通过HTTP cookie字段实现
- Session通过在服务器保存sessionid识别用户，cookie存储在客户端

\ | Cookie | Session
- | ------ | -------
储存位置 | 客户端 | 服务器端
目的 | 跟踪会话，也可以保存用户偏好设置或者保存用户名密码等 | 跟踪会话
安全性 | 不安全 | 安全

# 网络编程常考题

TCP/UDP socket编程；HTTP编程
- 了解TCP编程原理
- 了解UDP编程原理
- 了解如何发送HTTP请求

TCP socket编程原理
![](http://image30.360doc.com/DownloadImg/2011/06/0915/12646783_3.jpg) 


```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
client.sendall(b'hello')
data = client.recv(1024)
print(data)
client.close()
```


```python
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',8888))
server.listen()

while True:
    client, add = server.accept()
    print(client)
    timestr = time.ctime(time.time()) + '\r\n'
    client.send(timestr.encode())
    client.close()
server.close()
```

使用socket发送HTTP请求
- 使用socket接口发送HTTP请求
- HTTP建立在TCP基础之上
- HTTP是基于文本的协议


```python
import socket


server = socket.socket()
server.connect(('www.baidu.com', 80))

http = b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n'
server.sendall(http)
buf = server.recv(1024)
print(buf)
server.close()
```

    b'HTTP/1.1 200 OK\r\nAccept-Ranges: bytes\r\nCache-Control: no-cache\r\nConnection: Keep-Alive\r\nContent-Length: 14615\r\nContent-Type: text/html\r\nDate: Thu, 25 Jul 2019 07:46:01 GMT\r\nEtag: "5d2d5a1f-3917"\r\nLast-Modified: Tue, 16 Jul 2019 05:01:19 GMT\r\nP3p: CP=" OTI DSP COR IVA OUR IND COM "\r\nPragma: no-cache\r\nServer: BWS/1.1\r\nSet-Cookie: BAIDUID=63157C1BBA90D4D1B243BA295D4F0418:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com\r\nSet-Cookie: BIDUPSID=63157C1BBA90D4D1B243BA295D4F0418; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com\r\nSet-Cookie: PSTM=1564040761; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com\r\nVary: Accept-Encoding\r\nX-Ua-Compatible: IE=Edge,chrome=1\r\n\r\n<!DOCTYPE html><!--STATUS OK-->\r\n<html>\r\n<head>\r\n\t<meta http-equiv="content-type" content="text/html;charset=utf-8">\r\n\t<meta http-equiv="X-UA-Compatible" content="IE=Edge">\r\n\t<link rel="dns-prefetch" href="//s1.bdstatic.com"/>\r\n\t<link rel="dns-prefetc'
    

## IO多路复用常考题

物种IO网络模型
- Blocking IO 阻塞式
- Nonblocking IO 非阻塞式
- IO multiplexing 多路复用
- Signal Driven IO
- Asynchronous IO

IO多路复用
- 为了实现高并发需要一种机制并发处理多个socket
- Linux常见的是select/poll/epoll
    - 基本上select有3个缺点:
        - 连接数受限
        - 查找配对速度慢
        - 数据由内核拷贝到用户态
    - poll改善了第一个缺点
    - epoll改了三个缺点


```python
"""
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
        """
```




    '\nwhile True:\n    events = sel.select()\n    for key, mask in events:\n        callback = key.data\n        callback(key.fileobj, mask)\n        '



 Python封装了操作系统的IO多路复用
 - Python 的IO多路复用基于操作系统实现（select/poll/epoll）
 - Python2 select模块
 - Python3 selectors模块
     - 事件类型：EVENT_HEAD,EVENT_WRITE
     - DefaultSelector：自动根据平台选取合适的IO模型
         - register(fileobj, events, data=None)
         - unregister(fileobj)
         - modify(fileobj, events, data=None)
         - select(timeout=None):return\[(key,events)\]
         - close()

## Python并发网络库常考题

- Tornado并发网络库和同时也是一个web微框架
- Gevent绿色线程实现并发，猴子补丁修改内置socket
- Asyncio Python3内置的并发网络库，基于原生协程

Tornado框架
- 适用于微服务，实现Testful接口
- 底层基于Linux多路复用
- 可以通过协程或者回调实现异步编程
- 不过生态不完善，相应的异步框架比如ORM不完善

Gevent
- 基于轻量级绿色线程实现并发
- 需要注意monkey patch，gevent修改了内置的socket改为非阻塞
- 配合gunicorn和gevent部署作为wsgi server

Asyncio
- Python3引入到内置库，协程+事件循环
- 生态不够完善，没有大规模生产环境检验
- 目前应用不够广泛，基于Aiohttp可以实现一些小的服务


```python

```
