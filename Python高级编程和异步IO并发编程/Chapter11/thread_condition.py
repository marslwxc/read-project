import threading

# 条件变量，用于复杂的线程间同步 threading.Condition
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 好啊".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 君在长江尾".format(self.name))
            self.cond.notify()


class TianMap(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}: 小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 我们来对古诗吧".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 我在长江头".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    cond = threading.Condition()
    thread1 = TianMap(cond)
    thread2 = XiaoAi(cond)
    # 先调用condition.wait()的线程
    # 在调用with condition之后才能使用condition.wait()和condition.notify()
    # condition有两层锁，一把是底层锁，会在线程调用了wait方法的时候释放，
    # 上面的锁会在每次调用wait的时候分配一把并放入到等待队列中，等到notify方法的唤醒
    thread2.start()
    thread1.start()