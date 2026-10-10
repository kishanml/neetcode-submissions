class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        i = 0
        j = 0

        total_amount_of_water  =0
        curSum = 0

        while j < n-1:

            if height[i] == 0:
                i+=1
                j+=1

            if height[j+1] < height[i]:
                j+=1
                curSum += (height[i]-height[j])
            else:
                total_amount_of_water = curSum
                i = j+1
                j+=1

            # print(height[i],height[j],curSum,total_amount_of_water)
        return total_amount_of_water

            

