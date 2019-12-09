def gen_func():
    html = yield "hthp://www.baidu.com" 
    print(html)
    yield 2
    yield 3
    return 'end'

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, 'val')