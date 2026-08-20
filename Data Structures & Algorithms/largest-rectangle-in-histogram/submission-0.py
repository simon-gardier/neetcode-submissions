class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #
        #   X
        #   x
        #   x
        #   x       x
        #   x   x   x
        #   x   x x x x
        #   x x x x x x x x x x

        best_area = 0
        stack = []
    
        for i, height in enumerate(heights):
            start = i
            while len(stack) > 0 and height < stack[-1][1]:
                previous_best_index, previous_best_height = stack.pop()
                best_area = max(best_area, previous_best_height * (i - previous_best_index))
                start = previous_best_index
            stack.append((start, height))

        for previous_best_index, previous_best_height in stack:
            best_area = max(best_area, previous_best_height * (len(heights) - previous_best_index))

        return best_area


