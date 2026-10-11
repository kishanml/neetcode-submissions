class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        n = len(s)
        l = 0
        r = 0

        counter = {}
        max_repeats = 0
        longest_str_len = float('-inf')

        while r < n:

            counter[s[r]] = 1+ counter.get(s[r],0)
            max_repeats = max(max_repeats, counter[s[r]])

            while (r-l+1) - max_repeats >k:
                counter[s[l]]-=1
                l+=1
            longest_str_len = max(longest_str_len, r-l+1)
            r+=1
        return longest_str_len
            
