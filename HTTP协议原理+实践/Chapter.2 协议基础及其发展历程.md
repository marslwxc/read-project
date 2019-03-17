
# 网络协议分层

![经典五层模型](https://geekmubai-1253861834.cos.ap-shanghai.myqcloud.com/20180714105711.png)

- 物理层：主要作用是定义物理设备如何传输数据
- 数据链路层：在通信实体之间建立数据链路链接
- 网络层：为数据在结点之间的传输创建逻辑链路

- 传输层：TCP/IP协议，UDP协议
    1. 向用户提供可靠的端到端服务
    2. 传输层向高层屏蔽了下层数据通信的细节

- 应用层：
    1. 为应用软件提供了很多服务
    2. 构建与TCP协议之上
    3. 屏蔽网络传输的相关细节

# HTTP协议发展历史

## HTTP/0.9

只有一个命令GET

没有HEADER等描述数据的信息

服务器发送完毕，就关闭TCP连接

## HTTP/1.0

增加了很多命令

增加了status code和header

增加了多字符集支持、多部份发送、权限、缓存等

## HTTP/1.1

持久连接

pipeline（可以在同一个连接中发送多个请求）

增加host和其他一些命令

## HTTP2

所有的数据以二进制传输

同一个连接里面发送多个请求不需要按照顺序

头信息压缩以及推送等提高效率的功能

# HTTP三次握手

**防止服务端有无用的开销**

![HTTP三次握手](https://geekmubai-1253861834.cos.ap-shanghai.myqcloud.com/20180714113152.png)

- SYN=1:标志位，创建请求的数据包
- Seq=x:包
- ACK=x+1:应答

抓包三次握手分析
![抓包三次握手分析](https://geekmubai-1253861834.cos.ap-shanghai.myqcloud.com/Jietu20180714-113732.jpg)

# URI、URL、URN

## URI

**Uniform Resource Identifier/统一资源标志符**

用来唯一标识互联网上的信息资源

包含URL和URN

## URL

**Uniform Resource Locator/统一资源定位器**

http://user:pass@host.com:80/path?query=string#hash

格式：
- http:// ：使用怎样的协议进行访问
- user:pass@：用户认证，指定用户进行访问
- host.com：用来定位资源服务器在互联网中的位置
- :80：服务器端口，默认端口80
- /path：路由，定位服务器中查找内容的路径
- query=string：搜索参数
- hash：请求内容的某个片段

## URN

**永久统一资源定位符**

在资源移动之后还能被找到

# HTTP报文

![HTTP报文](https://geekmubai-1253861834.cos.ap-shanghai.myqcloud.com/20180714115244.png)

请求报文：
- 首行
    1. 请求方法（GET,POST,PUT,DELETE等）
    2. 请求资源地址
    3. 协议banben

响应报文：
- 首行
    1. 协议版本
    2. status code：请求状态 OK:状态具体含义

## HTTP方法

用来定义对于资源的操作

常用的有GET，POST等

从定义上讲有各自的语义

方法|描述
------|----
GET|请求指定的页面信息，并返回实体主体。
HEAD|类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
POST|向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
PUT|从客户端向服务器传送的数据取代指定的文档的内容。
DELETE|请求服务器删除指定的页面。
CONNECT|HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
OPTIONS|允许客户端查看服务器的性能。
TRACE|回显服务器收到的请求，主要用于测试或诊断。

## HTTP CODE

定义服务器对请求的处理结果

各个区间的CODE有各自的语义

好的HTTP服务可以通过CODE判断结果

状态码分类|分类描述
----------|--------
1**|信息，服务器收到请求，需要请求者继续执行操作
2**|成功，操作被成功接收并处理
3**|重定向，需要进一步的操作以完成请求
4**|客户端错误，请求包含语法错误或无法完成请求
5**|服务器错误，服务器在处理请求的过程中发生了错误

状态码|英文描述|中文描述
------|--------|--------
100|Continue|继续。客户端应继续其请求
101|Switching Protocols|切换协议。服务器根据客户端的请求切换协议。只能切换到更高级的协议，例如，切换到HTTP的新版本协议
||
200|OK|请求成功。一般用于GET与POST请求
201|Created|已创建。成功请求并创建了新的资源
202|Accepted|已接受。已经接受请求，但未处理完成
203|Non-Authoritative Information|非授权信息。请求成功。但返回的meta信息不在原始的服务器，而是一个副本
204|No Content|无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档
205|Reset Content|重置内容。服务器处理成功，用户终端（例如：浏览器）应重置文档视图。可通过此返回码清除浏览器的表单域
206|Partial Content|部分内容。服务器成功处理了部分GET请求
||
300|ultiple Choices|多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择
301|Moved Permanently|永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。今后任何新的请求都应使用新的URI代替
302|Found|临时移动。与301类似。但资源只是临时被移动。客户端应继续使用原有URI
303|See Other|查看其它地址。与301类似。使用GET和POST请求查看
304|Not Modified|未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源
305|Use Proxy|使用代理。所请求的资源必须通过代理访问
306|Unused|已经被废弃的HTTP状态码
307|Temporary Redirect|临时重定向。与302类似。使用GET请求重定向
||
400|Bad Request|客户端请求的语法错误，服务器无法理解
401|Unauthorized|请求要求用户的身份认证
402|Payment Required|保留，将来使用
403|Forbidden|服务器理解请求客户端的请求，但是拒绝执行此请求
404|Not Found|服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面
405|Method Not Allowed|客户端请求中的方法被禁止
406|Not Acceptable|服务器无法根据客户端请求的内容特性完成请求
407|Proxy Authentication Required|请求要求代理的身份认证，与401类似，但请求者应当使用代理进行授权
408|Request Time-out|服务器等待客户端发送的请求时间过长，超时
409|Conflict|服务器完成客户端的PUT请求是可能返回此代码，服务器处理请求时发生了冲突
410|Gone|客户端请求的资源已经不存在。410不同于404，如果资源以前有现在被永久删除了可使用410代码，网站设计人员可通过301代码指定资源的新位置
411|Length Required|务器无法处理客户端发送的不带Content-Length的请求信息
412|Precondition Failed|户端请求信息的先决条件错误
413|Request Entity Too Large|于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。如果只是服务器暂时无法处理，则会包含一个Retry-After的响应信息
414|Request-URI Too Large|求的URI过长（URI通常为网址），服务器无法处理
415|Unsupported Media Type|务器无法处理请求附带的媒体格式
416|Requested range not satisfiable|户端请求的范围无效
417|Expectation Failed|务器无法满足Expect的请求头信息
||
500|Internal Server Error|务器内部错误，无法完成请求
501|Not Implemented|务器不支持请求的功能，无法完成请求
502|Bad Gateway|为网关或者代理工作的服务器尝试执行请求时，从远程服务器接收到了一个无效的响应
503|Service Unavailable|于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的Retry-After头信息中
504|Gateway Time-out|当网关或代理的服务器，未及时从远端服务器获取请求
505|HTTP Version not supported|务器不支持请求的HTTP协议的版本，无法完成处理


```python
import socket

HOST = 'localhost'
PORT = 8080
ADDR = (HOST, PORT)

Web_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Web_Socket.bind(ADDR)
Web_Socket.listen(5)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = Web_Socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)
    
    http_response = b"""
    HTTP/1.1 200 OK\r\n
    \r\n
    Hello,world!
    """
    client_connection.send(http_response)
    client_connection.close()
Web_Socket.close()
```
