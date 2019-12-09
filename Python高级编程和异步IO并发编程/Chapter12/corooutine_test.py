def gen_func():
    html = yield "hthp://www.baidu.com" 
    print(html)
    yield 2
    yield 3
    return 'end'

# throw,close


# 1.生成器不知可以产出值，也可以接受值


if __name__ == "__main__": 
    gen = gen_func()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种：
    # 1. gen.send(None)
    # 2. next(gen)
    url = next(gen)
    print(url)
    html = 'html'
    # send方法可以传递值至生成器内部，还可以重启生成器执行到下一个yield的位置
    print(gen.send(html))    
    # 启动生成器的方式，next()、send
    # print(next(gen))
    # print(next(gen))