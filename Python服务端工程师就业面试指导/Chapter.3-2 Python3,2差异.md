
Python3改进
- print成为函数
- 编码问题。Python3不再有Unicode对象，默认str就是unicode
- 除法变化。Python3除号返回浮点数
- 类型注解（type hint）。帮助IDE实现类型检查
- 优化super()方便直接调用父类函数
- 高级解包操作。a,b,*rest = range(10)
- Keyword only arguments. 限定关键字参数
- Chained exceptions. Python3重新抛出异常不会丢失栈信息
- 一切返回迭代器(range,zip,map,dict.values,etc)are all iterators


```python
# print成为函数
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    
    


```python
# 类型注解（type hint）。帮助IDE实现类型检查
def hello(name:str) -> str:
    return 'hello ' + name

print(hello('me'))
```

    hello me
    


```python
# 高级解包操作。a,b,*rest = range(10)
a, b, *c = range(10)
print(a,b,c)
```

    0 1 [2, 3, 4, 5, 6, 7, 8, 9]
    


```python
# Keyword only arguments. 限定关键字参数
def add(a, b, *, c):
    return a+b+c

print(add(1,2,c=3))
```

    6
    


```python
# 一切返回迭代器range,zip,map,dict.values,etc are all iterators
print(range(10))
```

    range(0, 10)
    

Python3 新增
- yield from 链接子生成器
- asyncio内置库，async/await原生协程支持异步编程
- 新的内置库 enum，mock，asyncio，ipaddress，concurrent.futures等

Python3 改进
- 生成的pyc文件统一放到\__pycache__
- 一些内置库的修改。urllib，selector等
- 性能优化等

Python2/3兼容工具
- six模块
- 2to3等工具转换代码
- \__future__
