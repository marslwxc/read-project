class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:return []
        nums.sort()
        result = set()
        for k, v in enumerate(nums):
            s = {}
            for x in nums[k+1:]:
                if -v-x in s:
                    result.add((v, -v-x, x))
                else:
                    s[x] = 1
        return list(map(list, result))