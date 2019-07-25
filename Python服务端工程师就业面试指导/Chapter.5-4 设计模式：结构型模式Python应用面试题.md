
- 装饰器模式（Decorator）：无需子类化扩展对象功能
- 代理模式（Proxy）：把一个对象的操作代理到另一个对象
- 适配器模式（Adapter）：通过一个间接层适配统一接口
- 外观模式（Facade）：简化复杂对象的访问问题
- 享元模式（Flyweight）：通过对象复用（池）改善资源利用，比如连接池
- Model-View-Controller（MVC）：解耦展示逻辑和业务逻辑

代理模式
- 把一个对象的操作代理到另一个对象
- 通常使用has-a关系


```python
from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()
        
    def push(self, value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.pop()
        
    def empty(self):
        return len(self._deque) == 0
```

适配器模式
- 把不同对象的接口适配到同一个接口
- 当我们需要给不同的对象统一接口的时候可以使用适配器模式


```python
class Dog:
    def __init__(self):
        self.name = "Dog"
        
    def bark(self):
        return "woof"
    
    
class Cat:
    def __init__(self):
        self.name = 'Cat'
        
    def meow(self):
        return "meow"
    
    
class Adapter:
    def __init__(self, obj, **adaptered_methods):
        self.obj = obj
        self.__dict__.update(adaptered_methods)
        
    def __getattr__(self, attr):
        return getattr(self.obj, attr)
    
    
objects = []
dog = Dog()
objects.append(Adapter(dog, make_noise=dog.bark))
cat = Cat()
objects.append(Adapter(cat, make_noise=cat.meow))
for obj in objects:
    print("a {} goes {}".format(obj.name, obj.make_noise()))
```

    a Dog goes woof
    a Cat goes meow
    


```python

```
