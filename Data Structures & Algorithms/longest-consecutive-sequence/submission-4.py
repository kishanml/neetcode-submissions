from functools import reduce

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0


        nums = list(set(nums))
        if len(nums)==1:
            return 1
        nums.sort()
        n = len(nums)
        max_count = float('-inf')
        count = 0
        for i in range(1,n):
            if nums[i]-nums[i-1] == 1:
                count+=1
            else :
                count = 0
            max_count = max(max_count, count)

        return max_count + 1