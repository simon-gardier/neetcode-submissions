class Solution:
    def trap(self, height: List[int]) -> int:
        # water_total = 0

        # for i in range(len(height)):
        #     max_left = 0
        #     for j in range(i-1, -1, -1):
        #         max_left = max(height[j], max_left)

        #     max_right = 0
        #     for j in range(i+1, len(height)):
        #         max_right = max(height[j], max_right)

        #     min_max_height = min(max_left, max_right)
        #     if height[i] < min_max_height:
        #         water_total += min_max_height - height[i]

        # return water_total

        # water_total = 0
        # right_maximum = [0] * len(height)
        # left_maximum = [0] * len(height)

        # for i in range(1, len(height)):
        #     left_maximum[i] = max(height[i-1], left_maximum[i-1])

        # for i in range(len(height)-2, -1, -1):
        #     right_maximum[i] = max(height[i+1], right_maximum[i+1])

        # for i in range(len(height)):
        #     min_max_height = min(left_maximum[i], right_maximum[i])
        #     if height[i] < min_max_height:
        #         water_total += min_max_height - height[i]
        # return water_total

        water_total = 0
        max_left = height[0]
        max_right = height[-1]
        left, right = 0, len(height) - 1

        while left <= right:
            if max_left <= max_right:
                if height[left] < max_left:
                    water_total += max_left - height[left]
                else:
                    max_left = height[left]

                left += 1

            else:
                if height[right] < max_right:
                    water_total += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1

        return water_total
