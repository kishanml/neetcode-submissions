class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = [1 for _ in range(len(nums))]
        
        self_itr = 0
        while self_itr != len(nums):
            for i in range(len(nums)):
                if i != self_itr:
                    products[self_itr]*=nums[i]
            self_itr+=1 
        
        return products