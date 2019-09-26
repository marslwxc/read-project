class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self._gen(0, 0, n, "")
        return self.res
    
    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.res.append(result)
            return
        if left < n:
            self._gen(left+1, right, n, result+"(")
        if left > right and right < n:
            self._gen(left, right+1, n, result+")")