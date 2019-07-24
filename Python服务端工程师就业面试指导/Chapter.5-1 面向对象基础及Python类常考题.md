
Object Oriented Programming(OOP)
- 把对象作为基本单元，把对象抽象成类，包含成员和方法
- 数据封装、继承、多态
- Python中使用类来实现。过程式编程(函数)、OOP（类）

组合与继承
- 组合是使用其他的类实例作为自己的一个属性
- 子类继承父类的属性和方法
- 优先使用组合保持代码简单

类变量和实例变量的区别
- 类变量由所有实例共享
- 实例变量由实例单独享有，不同实例之间不影响
- 当我们需要在一个类的不同实例之间共享变量的时候使用类变量

classmethod/staticmethod区别
- 都可以通过Class.method()的方式使用
- classmethod第一个参量是cls，可以引用类变量
- staticmethod使用起来和普通函数一样，只不过放在类里去组织

什么是元类？使用场景
- 元类(Meta Class)是创建类的类
- 元类允许我们控制类的生成，比如修改类的属性
- 使用type来定义元类
- 元类最常见的一个使用场景就是ORM框架


```python
class Base:
    pass

class Child(Base):
    pass

#等价定义，注意Base后面要加上逗号
someChild = type('Child', (Base,), {})

#加上方法
class ChildWithMethod(Base):
    bor = True
    
    def hello(self):
        print('hello')
        
def hello(self):
    print('hello')
    
# 等价定义
ChildWithMethod = type(
    'ChildWithMethod', (Base,), {'bar':True, 'hello':hello}
)

class LowercaseMeta(type):
    """ 修改类的属性名称为小写的元类 """
    def __new__(mcs, name, bases, attrs):
        lower_attrs = {}
        for k, v in attrs.items():
            if not k.startswith('__'):
                lower_attrs[k.lower()] =  v
            else:
                lower_attrs[k] = v
        return type.__new__(mcs, name, bases, lower_attrs)
    

class LowercaseClass(metaclass=LowercaseMeta):
    BAR = True
    
    def HELLO(self):
        print('hello')
        
print(dir(LowercaseClass))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bar', 'hello']
    


```python

```
