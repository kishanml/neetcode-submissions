from collections import defaultdict
class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for ele in strs:
            count_arr = [0]*26
            for ch in ele:
                count_arr[ord(ch)-97]+=1
            hashmap[tuple(count_arr)].append(ele)
        return list(hashmap.values())


        
