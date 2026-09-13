
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for ele in nums:
            hashmap[ele] = 1+ hashmap.get(ele,0)
            
        freq = [[] for _ in range(len(nums)+1)]
        for key,v in hashmap.items():
            freq[v].append(key)
        
        ans = []
        for ent in range(len(freq)-1,0,-1):
            if freq[ent]:
                ans.append(freq[ent][0])
            if len(ans)==k:
                break

        return ans