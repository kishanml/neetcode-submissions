class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        i =0
        j = n-1
        water_accumulated = 0
        left_max = height[i]    
        right_max = height[j]

        while i<j:

            if left_max <= right_max:
                i+=1
                left_max = max(left_max, height[i])
                water_accumulated += left_max - height[i]
            else:
                j-=1
                right_max = max(right_max, height[j])
                water_accumulated += right_max - height[j]
            
            # print(left_max, right_max, i,j)
        return water_accumulated