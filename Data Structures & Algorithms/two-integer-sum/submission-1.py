class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i,ele in enumerate(nums):
            if ele not in hashmap:
                hashmap[target-ele] = i
            else:
                return [hashmap[ele], i]
        
 
        