from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Set = Counter(s1)
        m = len(s1)
        n = len(s2)

        for  i in range(n):
            probSubstr = set(s2[i:i+m])
            status = s1Set == Counter(probSubstr)
            if status:
                return True
            

        return False