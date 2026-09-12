class Solution:
    def climbStairs(self, n: int) -> int:
        
        one, two = 1,1

        for i in range(n-1):
            prev_one = one
            one = one+two
            two = prev_one

        return one

