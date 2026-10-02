class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # time complexity : O(len(s) + len(t))
        # space complexity : O(1)
        
        count_arr = [0]*26
        for ele in s:
            count_arr[ord(ele)-97]+=1

        for ele in t:
            count_arr[ord(ele)-97]-=1

        return all(ele==0 for ele in count_arr)
        