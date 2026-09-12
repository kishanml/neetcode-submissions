
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        
        for ele in nums:
            hashMap[ele] = 1+ hashMap.get(ele,0)

        sorted_hashMap = sorted(hashMap.items(), key=lambda x : x[1], reverse=True)[:k]
        return [ele[0] for ele in sorted_hashMap]
        
            
        