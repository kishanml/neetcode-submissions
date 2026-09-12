class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i,ele in enumerate(nums):
            to_find = target-ele
            if to_find not in hashMap:
                hashMap[ele] = i
            else:
                return [hashMap[to_find], i]


 
        