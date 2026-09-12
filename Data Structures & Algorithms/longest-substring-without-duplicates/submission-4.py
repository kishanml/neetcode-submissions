class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j = 0, 0
        n = len(s)
        longestSubstrLen = 0
        
        for i in range(n):
            ans = set()
            for j in range(i, n):
                if s[j] in ans:
                   break
                else:
                    ans.add(s[j])

            longestSubstrLen = max(longestSubstrLen, len(ans))
        return longestSubstrLen 
