class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_count = 0
        numSet = set(nums)

        for ele in nums:
            if ele-1 not in numSet:
                count = 0
                while (ele + count) in numSet:
                    count+=1

                max_count = max(max_count, count)

        return max_count
                