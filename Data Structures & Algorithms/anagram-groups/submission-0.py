from collections import defaultdict
class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        hashMap = defaultdict(list)

        for ele in strs:
            key_ = "".join(sorted(ele))
            hashMap[key_].append(ele)

        return list(hashMap.values())


        
