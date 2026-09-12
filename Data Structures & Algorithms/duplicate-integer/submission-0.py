class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsSet = set(nums)
        return True if len(numsSet)!=len(nums) else False