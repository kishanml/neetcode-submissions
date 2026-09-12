class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if nums == [0,0]:
            return [0,0]

        prodArr = []
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(n):
                if j!=i:
                    prod*=nums[j]
            prodArr.append(prod)
        return prodArr