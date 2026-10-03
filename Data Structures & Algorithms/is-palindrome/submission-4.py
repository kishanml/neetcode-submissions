class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(" ","")
        s = s.lower()
        
        n = len(s)

        if n==1:
            return True
        if n <= 2 and not s.isalpha():
            return True

        i=0
        j= n-1

        while i<=j:

            if not s[j].isalpha():
                j-=1
            
            if not s[i].isalpha():
                i+=1

            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                # print(s[i],s[j])
                return False
            print(s[i],s[j])
        return True