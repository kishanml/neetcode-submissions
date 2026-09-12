
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for val in nums:
            hashmap[val] = 1 + hashmap.get(val,0)
        
        freq = [[] for _ in range(len(nums)+1)]
        for key,v in hashmap.items():
            freq[v].append(key)
        # print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                res.extend(freq[i])
            if len(res)==k:
                return res
    