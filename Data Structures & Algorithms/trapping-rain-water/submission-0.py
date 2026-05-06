class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        for i, h in enumerate(height):
            if i == 0:
                leftMax[0] = h
            else:
                leftMax[i] = max(leftMax[i-1],h)
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                rightMax[i] = height[i]
            else:
                rightMax[i] = max(rightMax[i+1],height[i])
        # print(leftMax)
        # print(rightMax)
        for i in range(1,len(height)-1):
            water += max(0,min(leftMax[i-1], rightMax[i+1]) - height[i])

        return water