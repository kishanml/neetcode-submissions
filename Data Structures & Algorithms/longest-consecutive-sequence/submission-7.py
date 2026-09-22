class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_count = 0

        for ele in nums:
            if ele-1 not in nums:
                count = 0
                temp = ele+1
                while True:
                    if temp in nums:
                        count+=1
                        temp+=1
                    else:
                        break
                # print(ele,count)
            max_count = max(max_count, count+1)
        return max_count

