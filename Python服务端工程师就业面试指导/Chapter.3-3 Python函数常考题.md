
常考点：
- 参数传递
- （不）可变对象
- 可变参数

例题：
- 以下Python代码分别输出什么？


```python
# 可变类型作为参数
def flist(l):
    l.append(0)
    print(l)
    
l = []
flist(l)
flist(l)
```

    [0]
    [0, 0]
    


```python
# 不可变类型作为参数
def fstr(s):
    s += 'a'
    print(s)
    
s = "hehe"
fstr(s)
fstr(s)
```

    hehea
    hehea
    

Python如何传递参数
- Python唯一支持的参数传递是共享传参
- Call by Object(Call by Object Reference or Call by Sharing)
- Call by sharing(共享传参)。函数形参获得实参中各个引用的副本   

Python可变/不可变对象
- 不可变对象：bool/int/float/tuple/str/frozenset
- 可变对象：set/list/dict/

Python异常机制
1. BaseException
2. SystemExit/KeyboardInterrupt/GeneratorExit（系统相关异常）
3. Exception

使用异常的常见场景
- 网络请求（超时，连接错误）
- 资源访问（权限问题，资源不存在）
- 代码逻辑（越界访问、KeyError）

自定义异常
- 继承Exception实现自定义异常
- 给异常加上一些附加信息
- 处理一些业务相关的特定异常（raise MyException）

Python性能分析和优化
- GIL，Global Interpreter Lock
- Cpython解释器的内存管理并不是线程安全的
- 保护多线程情况下对Python对象的访问
- Cpython使用简单的锁机制避免多个线程同时执行字节码

GIL的影响：限制了程序的多核执行
- 同一时间只能有一个线程执行字节码
- CPU密集程序难以利用多核优势
- IO期间会释放GIL，对IO密集程序影响不大

如何规避GIL影响
- CPU密集可以使用多进程+进程池
- IO密集使用多线程/协程
- cpython扩展

分析程序性能
- 二八定律，大部分时间耗时在少量代码上
- 内置的profile/cprofile等工具
- 使用pyflame的火焰图工具

服务端性能优化措施
- 数据结构与算法优化
- 数据库层：索引优化，慢查询消除，批量操作减少IO，NoSQL
- 网络IO：批量操作，pipline操作减少IO
- 缓存：使用内存数据库redis/memcached
- 异步：asyncio，celery
- 并发：gevent/多线程

生成器 Generator
- 生成器就是可以生成值的函数
- 当一个函数里有了yield关键字就成了生成器
- 生成器可以挂起执行并且保持当前执行的状态

Python单元测试 Unit Testing
- 针对程序模块进行正确性检验
- 一个函数，一个类进行验证
- 自底向上保证程序正确性

单元测试库
- nose/pytest
- mock模块用来模拟替换网络请求
- coverage统计测试覆盖率

Python深拷贝和浅拷贝
- 什么是深拷贝？什么是浅拷贝？
- Python中如何实现深拷贝？
- Python中如何正确初始化一个二维数组？


```python

```
