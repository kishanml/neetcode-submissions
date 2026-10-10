class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        greater_ele_to_left = [0]*n
        left_max = 0
        for i in range(1,n):
            greater_ele_to_left[i] = left_max
            left_max = max(left_max, height[i])

        greater_ele_to_right = [0]*n
        right_max = 0
        for i in range(n-1,-1,-1):
            greater_ele_to_right[i] = right_max
            right_max = max(right_max, height[i])

        return sum( max(0,min(l,r)-h) for r,l,h in zip(greater_ele_to_right,greater_ele_to_left, height))