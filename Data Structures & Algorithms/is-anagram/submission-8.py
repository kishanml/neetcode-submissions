class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_arr = [0]*26
        for ele in s:
            count_arr[ord(ele)-97]+=1

        for ele in t:
            count_arr[ord(ele)-97]-=1

        return all(ele==0 for ele in count_arr)
        