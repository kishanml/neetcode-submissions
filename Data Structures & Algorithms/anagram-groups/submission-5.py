from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # time complexity O(N*K)
        # space complexity : 0(N*K)
        groups = defaultdict(list)
        for s in strs:
            count_arr = [0]*26
            for ele in s:
                count_arr[ord(ele)-97]+=1
            groups[tuple(count_arr)].append(s)

        return list(groups.values())
