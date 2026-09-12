from functools import reduce

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        numSet = set(nums)
        
        if len(numSet) == 1:
            return 1
        
        longestSeq = float('-inf')

        for ele in nums:

            if ele-1 not in numSet:

                count = 0
                while (ele + count) in numSet:
                    count+=1
                longestSeq = max(longestSeq, count)

        return longestSeq