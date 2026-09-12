from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = Counter(nums)

        return [ele[0] for ele in hashMap.most_common(k)]