class Solution:

    def count(self,n):
        count = 0
        while n:
            n &= n-1
            count+=1
        return count

    def countBits(self, n: int) -> List[int]:
        
        return [self.count(i) for i in range(n+1)]
