from collections import defaultdict
class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        hashMap = defaultdict(list)

        for ele in strs:
            count_arr = [0] * 26
            for c in ele:
                count_arr[ord(c)- ord('a')] +=1
            hashMap[tuple(count_arr)].append(ele)


        return list(hashMap.values())


        
