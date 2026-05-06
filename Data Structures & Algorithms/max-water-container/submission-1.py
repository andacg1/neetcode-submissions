class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        left = 0
        right = len(heights)-1
        while left < right:
            area = abs(right-left)*min(heights[left],heights[right])
            currMax = max(area, currMax)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return currMax
