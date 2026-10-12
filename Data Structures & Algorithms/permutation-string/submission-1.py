from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Set = set([ele for ele in s1])
        m = len(s1)
        n = len(s2)

        for  i in range(n):
            probSubstr = set(s2[i:i+m])
            diff = s1Set.difference(probSubstr)
            if not diff:
                return True

        return False