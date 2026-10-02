class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_arr = [0]*26
        for a,b in zip(s,t):
            count_arr[ord(a)-97]+=1
            count_arr[ord(b)-97]-=1

        return all(ele==0 for ele in count_arr)