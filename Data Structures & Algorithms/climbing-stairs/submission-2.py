class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n

        def climb( current_stair : int):
            
            if current_stair>=n:
                return current_stair==n
            
            if cache[current_stair]!=-1:
                return cache[current_stair]
            
            cache[current_stair] = climb(current_stair+1) + climb(current_stair+2)
            return cache[current_stair]

        return climb(0)


