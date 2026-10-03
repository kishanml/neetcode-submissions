class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(" ","")
        s = s.lower()
        
        n = len(s)

        if n ==1:
            return True

        i=0
        j= n-1

        while i<j:

            while i<j and not s[i].isalnum():
                i+=1
            while j>i and not s[j].isalnum():
                j-=1

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1


        return True