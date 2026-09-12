class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_arr = [0]*26

        for chr_s in s:
            count_arr[ord(chr_s)-97]+=1
        for chr_t in t:
            count_arr[ord(chr_t)-97]-=1

        for value in count_arr:
            if value!=0:
                return False
    
        return True