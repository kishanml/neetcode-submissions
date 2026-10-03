class Solution:
    
    def two_sum(self,ans, nums,k, i,j , target):

        while i<j:

            cursum = nums[k] + nums[i] + nums[j]
            if cursum == target:
                ans.append([nums[k] , nums[i] , nums[j]])
                i+=1
                j-=1

            elif cursum > target:
                j-=1
            else:
                i+=1
        return None

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue 

            self.two_sum(ans, nums,i,i+1,n-1,0)
            
        return ans

