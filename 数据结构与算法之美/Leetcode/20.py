class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for x in s:
            if x not in dic:
                stack.append(x)
            elif not stack or dic[x] != stack.pop():
                return False
        return not stack