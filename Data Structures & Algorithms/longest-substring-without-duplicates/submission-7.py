class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        hashmap = {}

        l= 0
        n = len(s)
        max_len = 0

        for r in range(n):
            
            if s[r] in hashmap:
                l = max(hashmap[s[r]]+1, l)

            hashmap[s[r]] = r
            max_len = max(max_len, r - l+1)
        return max_len
            
            
        