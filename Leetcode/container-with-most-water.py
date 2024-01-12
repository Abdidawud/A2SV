class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        _max = 0
        while left < right:
            water = (right-left)*min(height[left], height[right])
            _max = max(_max, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return _max