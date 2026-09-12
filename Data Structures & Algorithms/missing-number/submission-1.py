class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        pool = list(range(len(nums)+1)) + nums

        res = 0
        for ele in pool:
            res ^= ele
        print(res)
        return res