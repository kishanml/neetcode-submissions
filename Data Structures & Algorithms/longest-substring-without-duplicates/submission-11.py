class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        
        hashmap = {}
        l = 0
        n = len(s)
        res = 0

        for i in range(n):
            if s[i] in hashmap:
                l = max(hashmap[s[i]]+1,l)
            
            hashmap[s[i]] = i
            res = max(res, i-l+1)
        return res
            
        