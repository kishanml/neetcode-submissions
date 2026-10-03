class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(" ","")
        s = s.lower()
        alphanum_free_s = ""
        for ele in s:
            if ele.isalnum():
                alphanum_free_s += ele
        return alphanum_free_s==alphanum_free_s[::-1]