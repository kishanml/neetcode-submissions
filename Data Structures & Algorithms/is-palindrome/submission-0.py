import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True
        s = re.sub(r'[^A-Za-z0-9]','',s)
        s = s.lower()
        n = len(s)

        i = 0
        j = n-1

        while i<=j:

            if s[i] != s[j]:
                return False
                break

            i+=1
            j-=1

        return True