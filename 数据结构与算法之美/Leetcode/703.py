import heapq

class KthLargest:
    def __init__(self, k: int, nums):
        self.pool = heapq.nlargest(k, nums)[::-1] #hi，我是一丢丢。。。。
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0] 


"""
heapq.heappush(heap,item):将item，推入heap
heapq.heappop(heap)：将heap的最小值pop出heap，heap为空时报IndexError错误
heapq.heappushpop(heap,item)：pop出heap中最小的元素，推入item
heapq.heapify(x)：将list X转换为heap
heapq.heapreplace(heap,item)：pop出最小值，推入item，heap的size不变
heapq.merge(*iterable)：将多个可迭代合并，并且排好序，返回一个iterator
heapq.nlargest(n,iterable,key)：返回item中大到小顺序的前N个元素，key默认为空，可以用来指定规则如：function等来处理特定的排序
heapq.nsmallest(n,iterable,key)：返回item中小到大顺序的前N个元素，key默认为空，可以用来指定规则如：function等来处理特定的排序
"""