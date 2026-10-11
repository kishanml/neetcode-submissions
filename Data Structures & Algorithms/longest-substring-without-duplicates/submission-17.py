class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        n = len(s)
        
        i =0
        j =0

        mapper  ={}
        longestSubstringLen = 0

        while j<n:
            
            if s[j] in mapper:
                i = mapper[s[j]]+1
            mapper[s[j]] = j
            longestSubstringLen = max(longestSubstringLen, j-i+1)
            j+=1
            
        return longestSubstringLen
                
