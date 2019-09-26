class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:return 0
        start, end = prices[0], prices[0]
        res = 0
        for x in prices:
            if x < end:
                res = res + end - start
                start, end = x, x
            else:
                end = x
        res = res + end - start
        return res