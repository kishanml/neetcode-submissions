class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_count = 0
        for ele in nums:
            if ele-1 not in nums:
                count = 0
                while (ele + count) in nums:
                    count+=1

                max_count = max(max_count, count)

        return max_count
                