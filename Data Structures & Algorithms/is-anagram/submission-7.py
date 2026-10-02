class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_arr_a = [0]*26
        count_arr_b = [0]*26
        for a,b in zip(s,t):
            count_arr_a[ord(a)-97]+=1
            count_arr_b[ord(b)-97]+=1

        return count_arr_a == count_arr_b