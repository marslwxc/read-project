class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for k, v in enumerate(nums):
            y = target - v
            if y in s:
                return [s[y], k]
            else:
                s[v] = k