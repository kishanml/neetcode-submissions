
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        freq = [[]] * (len(nums)+1)
        for key, value in counter.items():
            freq[value] = key
        ans = []
        for i in range(len(freq)-1,-1,-1):
            if freq[i]:
                ans.append(freq[i])
            if len(ans) == k:
                return ans
        return nums