
Decorator
- Python中一切皆对象，函数也可以当作参数传递
- 装饰器是接受一个函数作为参数，添加功能后返回一个新函数的函数
- Python中通过@使用装饰器


```python
# 编写一个记录函数耗时的装饰器
import time

def log_time(func):
    def _log(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("used time {}".format(end-start))
        return res
    return _log


@log_time
def mysleep():
    time.sleep(1)
    
mysleep()
```

    used time 1.000128984451294
    


```python
import time


class LogTime:
    
    def __call__(self, func):
        def _log(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            print("used time {}".format(end-start))
            return res
        return _log
    

@LogTime()
def mysleep():
    time.sleep(1)
    
mysleep()
```

    used time 1.0004043579101562
    

可以使用类装饰器比较方便地实现装饰器参数


```python
import time


class LogTime:
    
    def __init__(self, use_int=False):
        self.use_int = use_int
    
    def __call__(self, func):
        def _log(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            if self.use_int:
                print("used time {}".format(int(end-start)))
            else:
                print("used time {}".format(end-start))
            return res
        return _log
    

@LogTime(True)
def mysleep():
    time.sleep(1)
    
mysleep()
```

    used time 1
    


```python

```
