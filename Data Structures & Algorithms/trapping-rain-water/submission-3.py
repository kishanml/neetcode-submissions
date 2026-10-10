class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        greater_ele_to_left = [0]*n
        greater_ele_to_left[0] = height[0]
        for i in range(1,n):
            greater_ele_to_left[i] = max(greater_ele_to_left[i-1], height[i])

        greater_ele_to_right = [0]*n
        greater_ele_to_right[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            greater_ele_to_right[i] = max(greater_ele_to_right[i+1], height[i])

        return sum( max(0,min(l,r)-h) for r,l,h in zip(greater_ele_to_right,greater_ele_to_left, height))