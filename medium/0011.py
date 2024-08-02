class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        area = 0
        for i in range(len(height)):
            if height[left] < height[right]:
                area = max(area, height[left] * (right - left))
                left += 1
            else:
                area = max(area, height[right] * (right - left))
                right -= 1
        return area
