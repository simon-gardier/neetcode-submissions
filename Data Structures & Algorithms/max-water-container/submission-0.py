class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        current_best_area = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            current_best_area = max(current_best_area, min_height * (right - left))
            if heights[left] == min_height:
                left += 1
            else:
                right -= 1
        return current_best_area