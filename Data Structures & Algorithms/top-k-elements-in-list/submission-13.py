
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        freq = [[] for _ in range(len(nums)+1)]
        for key, value in counter.items():
            freq[value].append(key)

        # print(freq)
        ans = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                ans.extend(freq[i])
            if len(ans) == k:
                return ans
        return nums