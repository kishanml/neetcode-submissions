class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        n = len(s)
        
        i =0
        j =0

        curSet = set()
        longestSubstringLen = 0

        while j<n:
            
            while s[j] in curSet:
                curSet.remove(s[i])
                i+=1
            curSet.add(s[j])
            longestSubstringLen = max(longestSubstringLen, j-i+1)
            j+=1
            
        return longestSubstringLen
                
