
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        
        for ele in nums:
            hashMap[ele] = 1+ hashMap.get(ele,0)

        freq = [[] for i in range(len(nums)+1)]
        for key,v in hashMap.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                res.extend(freq[i])
                if len(res) == k:
                    return res
                