class Solution:
    
    def two_sum(self,ans, nums,k, i,j , target):

        while i<j:

            cursum = nums[k] + nums[i] + nums[j]
            if cursum == target:
                ans.append([nums[k] , nums[i] , nums[j]])
                i+=1
                j-=1

                while i<j and nums[i] == nums[i-1]:
                    i+=1
                while i<j and nums[j]== nums[j+1]:
                    j-=1

            elif cursum > target:
                j-=1
            else:
                i+=1
        return None

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Time complexity : 0(n^2)
        # Space complexity : 0(n^2 ) including output


        n = len(nums)
        nums.sort() #O(nlogn)

        ans = []
        for i in range(n-2): #O(n)
            if i>0 and nums[i] == nums[i-1]:
                continue 

            self.two_sum(ans, nums,i,i+1,n-1,0) #(O(n))
            
        return ans

