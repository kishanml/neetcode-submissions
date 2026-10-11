class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        n = len(s)
        if n == 1:
            return 1
        
        i =0
        j =0

        curSet = set()
        longestSubstringLen = 0

        while j<n:

            if s[j] not in curSet:
                curSet.add(s[j])
                j+=1
            else:
                longestSubstringLen = max(longestSubstringLen, j-i)
                curSet = set()
                i = j
               

            # print(i,j,curSet, longestSubstringLen)
        longestSubstringLen = max(longestSubstringLen, j-i)

        return longestSubstringLen
                
