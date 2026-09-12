from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for s in strs:

            countarr = [0]*26
            for ch in s:
                countarr[ord(ch)-ord('a')]+=1
            
            hashmap[tuple(countarr)].append(s)

        return list(hashmap.values())
