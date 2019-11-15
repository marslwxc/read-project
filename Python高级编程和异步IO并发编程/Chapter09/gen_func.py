# 生成器函数：函数里只要有yield关键字；
def gen_func():
    yield 1
    yield 2
    yield 3
# 惰性求值，延迟求值提供了可能

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == "__main__":
    # 生成器对象，python编译字节码的时候产生
    gen = gen_func()
    for value in gen:
        print(value)