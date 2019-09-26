class Solution:
    def totalNQueens(self, n: int) -> int:
        if n<1: return []
        self.result = []
        self.cols, self.pie, self.na = set(), set(), set()
        self.DFS(n, 0, [])
        return len(self.result)
    
    def DFS(self, n, row, res):
        if row >= n:
            self.result.append(res)
            return
        
        for col in range(n):
            if col in self.cols or col + row in self.pie or row - col in self.na:
                continue
                
            self.cols.add(col)
            self.pie.add(col + row)
            self.na.add(row - col)
            
            self.DFS(n, row + 1, res + [col])
            
            self.cols.remove(col)
            self.pie.remove(col + row)
            self.na.remove(row - col)