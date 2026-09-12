class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_arr = [0]*26
        s= s.upper()
        t= t.upper()

        for chr_a in s:
            count_arr[ord(chr_a)-65]+=1
        
        for chr_b in t:
            count_arr[ord(chr_b)-65]-=1

        for val in count_arr:
            if val!=0:
                return False
        return True
        