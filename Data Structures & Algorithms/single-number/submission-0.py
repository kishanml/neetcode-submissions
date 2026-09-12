class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        first_ele = 0
        for ele in nums:
            first_ele = first_ele ^ ele
            print(first_ele)
        return first_ele