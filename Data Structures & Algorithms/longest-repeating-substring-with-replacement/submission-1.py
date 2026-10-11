class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        


        n = len(s)
        longestsubstr  = float('-inf')
        for i in range(n):
            mapper = {}

            for j in range(i,n):
                mapper[s[j]] =  1 + mapper.get(s[j],0)
            
                if (j-i+1)- mapper[s[j]] <= k:
                    longestsubstr  = max(longestsubstr, j-i+1)
        return longestsubstr