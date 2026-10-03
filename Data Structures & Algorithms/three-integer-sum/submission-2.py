class Solution:
    
    def two_sum(self, nums, i,j , target):

        while i<j:

            cursum = nums[i-1] + nums[i] + nums[j]
            if cursum == target:
                return [nums[i-1] , nums[i] , nums[j]]
            elif cursum > target:
                j-=1
            else:
                i+=1
        return []

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):

            idxs = self.two_sum(nums,i+1,n-1,0)
            if idxs:
                if idxs not in ans:
                    ans.append(idxs)
        return ans

