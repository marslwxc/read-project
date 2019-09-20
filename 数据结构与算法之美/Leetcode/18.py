class Solution:
    def fourSum(self, nums, target: int):
        if len(nums) < 4: return []        
        nums.sort()
        ans=set()
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):#固定两个数
                left=j+1#左指针
                right=len(nums)-1#右指针
                while(right>left):
                    temp=nums[i]+nums[j]+nums[left]+nums[right]
                    if temp==target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    if temp>target:right-=1#太大了，右指针左移
                    if temp<target:left+=1#反之

        return list(map(list, ans))


test = Solution()
test_list = [1,0,-1,0,-2,2]
target = 0
result = test.fourSum(test_list, target)
print(result)