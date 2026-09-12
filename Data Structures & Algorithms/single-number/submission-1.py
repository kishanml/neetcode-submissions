class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unique_ele = 0
        for ele in nums:
            unique_ele ^= ele
        return unique_ele