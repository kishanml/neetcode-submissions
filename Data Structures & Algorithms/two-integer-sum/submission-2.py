class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numRecord = {}
        
        for i,ele in enumerate(nums):
            to_find = target-ele
            if ele not in numRecord:
                numRecord[to_find]= i
            else:
                return [numRecord[ele],i]
