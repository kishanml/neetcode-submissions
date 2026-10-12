class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = sorted(s1)

 
        m = len(s2)

        for i in range(m):
            for j in range(i,m):
                probStr = sorted(s2[i:j+1])
                if probStr  == s1:
                    return True
        return False