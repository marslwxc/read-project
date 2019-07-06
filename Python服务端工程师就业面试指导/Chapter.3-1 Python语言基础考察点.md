
## Python语言特性

- 动态强类型语言
    - 动态还是静态指的是编译期还是运行期确定类型
    - 强类型指的是不会发生隐式类型转换

- Python作为后端语言优缺点
    - 胶水语言，轮子多，应用广泛
    - 语言灵活，生产力高
    - 性能问题，代码维护问题，python2/3兼容问题

- 鸭子类型：当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来像鸭子、那么这只鸟就可以被称为鸭子
    - 鸭子类型更关系的是接口而非类型
    - 关注点在对象的行为，而不是类型（duck typing）
    - 比如：file，StringIO，socket对象都支持read/write方法（file like object）
    - 再比如定义了__iter__魔术方法的对象可以用for迭代


```python
class Duck:
    def quack(self):
        print("gua gua")
        
        
class Person:
    def quack(self):
        print("person:gua gua")
        
        
def in_the_forest(duck):
    duck.quack()
    
    
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
    print(type(donald), type(john))
    print(isinstance(donald, Duck), isinstance(john, Person))
    
    
game()
```

    gua gua
    person:gua gua
    <class '__main__.Duck'> <class '__main__.Person'>
    True True
    

- monkey patch
    - 所谓的monkey patch就是运行时替换
    - 比如gevent库需要修改内置的socket
    - from gevent import monkey；monkey.patch_socket()


```python
import socket
print(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_select()
print("After moneky patch")
print(select.select)
```

    <class 'gevent._socket3.socket'>
    After monkey patch
    <class 'gevent._socket3.socket'>
    <built-in function select>
    After moneky patch
    <function select at 0x000002B11FFEDEA0>
    


```python
import time
print(time.time())

def _time():
    return 1234

time.time = _time
print(time.time())
```

    1562421063.0840535
    1234
    

- 自省 Introspection
    - 运行时判断一个对象的类型的能力
    - python一切皆对象，用type，id，isinstance获取对象类型信息
    - Inspect模块提供了更多获得对象信息的函数


```python
l1 = [1,2,3]
d = dict(a=1)

print(type(l1), type(d))
print(isinstance(l1, list), isinstance(d, dict))

def add(a,b):
    if isinstance(a, int):
        return a + b
    elif isinstance(a, str):
        return a.upper() + b
    
print(add(1,2), add('head', 'tail'))
print(id(l1), id(d))
```

    <class 'list'> <class 'dict'>
    True True
    3 HEADtail
    1789215104712 1789215986672
    

- 列表或字典推导 List or Dict Comprehension
    - [i for i in range(10 if i%2 == 0]
    - 一种快速生成list/dict/set的方式，用来替代map/filter等
    - （i for i in range(10 if i%2 == 0）返回生成器


```python
a = ['a','b','c']
b = [1,2,3]

c = [i for i in range(10)]
d = {k:v for k,v in zip(a,b)}
e = (i for i in range(10))
print(c, d, type(e))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] {'a': 1, 'b': 2, 'c': 3} <class 'generator'>
    

- Python之禅 The Zen of Python
    - python编程准则
    - import this


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    

Python之禅 by Tim Peters
 
优美胜于丑陋（Python 以编写优美的代码为目标）

明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）

简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）

复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）

扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）

间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）

可读性很重要（优美的代码是可读的）

即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）

不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
 
当存在多种可能，不要尝试去猜测

而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）

虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
 
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
 
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
 
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
