class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        l = 0
        r = n-1
        max_water = -1
        
        while l<=r:

            max_water = max(max_water, (r-l)* min(heights[r], heights[l]))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_water

